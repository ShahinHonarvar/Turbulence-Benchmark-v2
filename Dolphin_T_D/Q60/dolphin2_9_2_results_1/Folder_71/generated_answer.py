def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[22]
    prime_list = []
    for i in range(x, 1, -1):
        str_i = str(i)
        if '0' not in str_i:
            for j in range(len(str_i) - 1, -1, -1):
                if is_prime(int(str_i[j:])) and is_prime(int(str_i[:j])):
                    prime_list.append(int(str_i))
    return sorted(prime_list, reverse=True)
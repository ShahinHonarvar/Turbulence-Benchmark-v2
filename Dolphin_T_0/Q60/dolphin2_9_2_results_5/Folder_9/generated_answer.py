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
    x = t[29]
    prime_list = []
    for num in range(2, x + 1):
        if '0' in str(num) or not is_prime(num):
            continue
        while len(str(num)) > 1:
            if not is_prime(int(str(num)[1:-1])):
                break
            num = int(str(num)[1:-1])
        else:
            prime_list.append(num)
    return sorted(prime_list, reverse=True)
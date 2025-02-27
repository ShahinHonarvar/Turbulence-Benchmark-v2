def all_left_truncatable_prime(tup):
    x = tup[52]
    prime_list = []
    for num in range(x - 1, 1, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        else:
            z = True
            while str_num:
                if not is_prime(int(str_num)):
                    z = False
                    break
                str_num = str_num[1:]
            if z:
                prime_list.append(num)
    return sorted(prime_list, reverse=True)

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
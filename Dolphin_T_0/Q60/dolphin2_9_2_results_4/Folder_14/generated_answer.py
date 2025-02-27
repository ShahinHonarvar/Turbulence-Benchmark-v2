def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_right_truncatable_prime(t):
    primes, x = ([], t[78])
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        while len(str_num) > 1:
            if not is_prime(int(str_num)):
                break
            str_num = str_num[1:-1]
        if len(str_num) == 1 and is_prime(int(str_num)):
            primes.append(num)
    return sorted(primes, reverse=True)
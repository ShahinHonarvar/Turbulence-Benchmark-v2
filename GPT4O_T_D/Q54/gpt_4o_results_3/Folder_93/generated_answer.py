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

def all_right_truncatable_prime(t):
    if len(t) <= 11:
        return []
    x = t[11]
    right_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        is_truncatable = True
        while str_num:
            if not is_prime(int(str_num)):
                is_truncatable = False
                break
            str_num = str_num[:-1]
        if is_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
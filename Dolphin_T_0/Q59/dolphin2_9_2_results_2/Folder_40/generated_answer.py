def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(a):
    x = a[10]
    truncatable_primes = [11]
    i = 11
    while i < x:
        i += 1
        if is_prime(i):
            trunct_num = i
            still_ok = 1
            while still_ok and trunct_num:
                still_ok = is_prime(trunct_num)
                trunct_num //= 10
            if still_ok:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
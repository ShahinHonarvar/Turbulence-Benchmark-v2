def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def all_right_truncatable_prime(a):
    x = a[52]
    trunc_primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc > 1:
                trunc //= 10
                if not is_prime(trunc):
                    break
                if trunc == 2:
                    trunc_primes.append(num)
                    break
    return sorted(trunc_primes, reverse=True) if len(trunc_primes) > 0 else []
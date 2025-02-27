def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(x):
    trunc_primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            trunc = num
            while trunc != 0 and trunc != 2 and (trunc != 3) and (trunc != 5) and (trunc != 7):
                trunc //= 10
            if trunc == 0 or trunc == 2 or trunc == 3 or (trunc == 5) or (trunc == 7):
                trunc_primes.append(num)
    return sorted(trunc_primes, reverse=True)
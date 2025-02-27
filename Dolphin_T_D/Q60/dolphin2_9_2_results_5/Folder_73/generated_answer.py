def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[97]
    primes = []
    for n in range(2, x + 1):
        if '0' not in str(n):
            trunc = n
            while trunc > 1:
                if is_prime(trunc):
                    primes.append(n)
                trunc = trunc // 10
    primes = list(set(primes))
    primes.sort()
    return primes
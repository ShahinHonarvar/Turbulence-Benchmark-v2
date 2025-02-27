def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_zero_free(n):
    while n > 0:
        if n % 10 == 0:
            return False
        n //= 10
    return True

def calculate_truncatable_primes(limit):
    truncatable_primes = []
    for n in range(2, limit):
        if is_prime(n) and is_zero_free(n):
            truncatable = True
            left = n
            right = n
            while left > 10 and right > 10:
                left //= 10
                right = int(str(right)[1:])
                if not (is_prime(left) and is_prime(right)):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)
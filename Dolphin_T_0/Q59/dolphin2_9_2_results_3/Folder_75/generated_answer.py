def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    sq = int(n ** 0.5) + 1
    for divisor in range(3, sq, 2):
        if n % divisor == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[41]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            trunc = i
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
                if trunc == 0:
                    left_truncatable_primes.append(i)
    left_truncatable_primes.sort()
    return left_truncatable_primes
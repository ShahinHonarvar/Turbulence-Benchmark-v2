def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_truncatable_primes():
    truncatable_primes = []
    for n in range(99999983, 0, -2):
        if is_prime(n) and (not '0' in str(n)):
            left_truncatable = True
            right_truncatable = True
            for i in range(1, len(str(n))):
                if not is_prime(int(str(n)[:-i])):
                    left_truncatable = False
                    break
            for i in range(1, len(str(n))):
                if not is_prime(int(str(n)[i:])):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)
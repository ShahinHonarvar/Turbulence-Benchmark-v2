def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(x):
    primes = []
    for n in range(2, x):
        if is_prime(n) and '0' not in str(n):
            truncatable = True
            digits = list(str(n))
            for i in range(1, len(digits)):
                if not is_prime(int(''.join(digits[i:]))):
                    truncatable = False
                    break
            if truncatable:
                primes.append(n)
    return sorted(primes, reverse=True)
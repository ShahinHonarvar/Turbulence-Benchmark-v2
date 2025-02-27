def all_left_right_truncatable_prime(x):
    primes = [i for i in range(2, x + 1) if all((n not in str(i) for n in '024568'))]
    truncatable_primes = []
    for prime in primes:
        if is_left_and_right_truncatable_prime(prime, len(str(prime)) - 1):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(prime, digits):
    if digits == 1 or digits == 2:
        return True
    for i in range(1, digits):
        left = int(str(prime)[:i])
        right = int(str(prime)[-i:])
        if not is_prime(left) or not is_prime(right) or '0' in str(prime):
            return False
    return is_prime(prime)
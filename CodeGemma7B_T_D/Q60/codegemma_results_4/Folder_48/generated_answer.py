def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    result = []
    for prime in primes:
        str_prime = str(prime)
        if '0' not in str_prime and len(str_prime) > 1:
            for i in range(1, len(str_prime)):
                left, right = (int(str_prime[:i]), int(str_prime[i:]))
                if is_prime(left) and is_prime(right):
                    result.append(prime)
                    break
    return sorted(result)
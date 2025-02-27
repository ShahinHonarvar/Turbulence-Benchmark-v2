def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    result = []
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        is_truncatable = True
        for i in range(1, len(str_prime)):
            left_prime = int(str_prime[:i])
            right_prime = int(str_prime[i:])
            if not is_prime(left_prime) or not is_prime(right_prime):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(prime)
    return sorted(result, reverse=True)
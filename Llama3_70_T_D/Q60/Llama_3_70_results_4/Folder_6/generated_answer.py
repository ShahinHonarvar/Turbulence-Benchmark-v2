def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[74]
    primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        is_truncatable = True
        for i in range(1, len(str_prime)):
            left_truncated = int(str_prime[i:])
            right_truncated = int(str_prime[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    return truncatable_primes
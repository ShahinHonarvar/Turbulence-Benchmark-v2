def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[4]
    primes = [i for i in range(10, x) if is_prime(i)]
    left_truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        if '0' in prime_str:
            continue
        is_left_truncatable = True
        for i in range(1, len(prime_str)):
            if not is_prime(int(prime_str[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)
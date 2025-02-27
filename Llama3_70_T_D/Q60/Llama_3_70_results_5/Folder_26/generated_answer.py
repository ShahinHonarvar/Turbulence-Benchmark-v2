def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[81]
    left_right_truncatable_primes = set()
    for prime in range(11, x + 1):
        if '0' in str(prime):
            continue
        str_prime = str(prime)
        left_truncatable = True
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])):
                left_truncatable = False
                break
        if not left_truncatable:
            continue
        right_truncatable = True
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[:-i])):
                right_truncatable = False
                break
        if right_truncatable:
            left_right_truncatable_primes.add(prime)
    return sorted(list(left_right_truncatable_primes), reverse=True)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[803]
    right_truncatable_primes = []

    def is_right_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes)
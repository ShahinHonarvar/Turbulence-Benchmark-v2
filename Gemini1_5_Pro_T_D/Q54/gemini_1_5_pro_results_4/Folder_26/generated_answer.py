def all_right_truncatable_prime(numbers):
    x = numbers[81]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        for i in range(1, len(str(n)) + 1):
            if not all((n % j for j in range(2, int(str(n)[:i]) ** 0.5 + 1))):
                return False
        return True
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
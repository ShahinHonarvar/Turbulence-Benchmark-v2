def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[35]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable = []
    for p in primes:
        if all((is_prime(int(str(p)[:-i])) for i in range(1, len(str(p)) + 1))):
            right_truncatable.append(p)
    return sorted(right_truncatable, reverse=True)
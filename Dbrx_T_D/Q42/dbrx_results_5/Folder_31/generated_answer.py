def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors = set()
    for _ in numbers[:65]:
        prime_factors.update((x for x in numbers[66] if is_prime(x) and x <= numbers[66]))
    return prime_factors
def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        f = []
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                f.append(i)
                if i != n // i:
                    f.append(n // i)
        return f
    number = numbers[222]
    all_factors = factors(number)
    prime_factors_set = set([i for i in all_factors if is_prime(i)])
    return prime_factors_set
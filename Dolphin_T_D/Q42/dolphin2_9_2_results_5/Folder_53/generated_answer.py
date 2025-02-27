def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target_number = numbers[73]
    factors = set()
    for i in range(1, target_number + 1):
        if target_number % i == 0:
            sub_factors = [j for j in range(1, i + 1) if i % j == 0]
            if is_prime(i) and len(sub_factors) == 2:
                factors.add(i)
    return factors
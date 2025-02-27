def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = set()

    def prime_factors_recursive(n, i):
        if i > n:
            return
        if is_prime(i) and n % i == 0:
            prime_numbers.add(i)
        prime_factors_recursive(n, i + 1)
    prime_factors_recursive(numbers[7], 2)
    return prime_numbers
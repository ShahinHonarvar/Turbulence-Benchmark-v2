def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_factors(n):
        factors = []
        for i in range(2, n + 1):
            while n % i == 0:
                factors.append(i)
                n //= i
        return factors
    prime_factors_set = set()
    for num in find_factors(numbers_list[63]):
        if is_prime(num):
            prime_factors_set.add(num)
    return prime_factors_set
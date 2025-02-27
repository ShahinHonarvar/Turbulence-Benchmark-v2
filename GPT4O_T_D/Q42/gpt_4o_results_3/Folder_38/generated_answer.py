def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_prime_factors(n):
        factors = set()
        div = 2
        while div * div <= n:
            while n % div == 0:
                if is_prime(div):
                    factors.add(div)
                n //= div
            div += 1
        if n > 1:
            factors.add(n)
        return factors
    number_at_index_38 = numbers[38]
    return get_prime_factors(number_at_index_38)
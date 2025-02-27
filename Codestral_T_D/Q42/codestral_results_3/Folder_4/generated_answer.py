def prime_factors(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n = n // 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n = n // i
        if n > 2:
            factors.add(n)
        return factors
    return get_factors(num_list[15])
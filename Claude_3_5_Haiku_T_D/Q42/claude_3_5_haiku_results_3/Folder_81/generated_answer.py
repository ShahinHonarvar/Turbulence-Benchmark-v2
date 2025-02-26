def prime_factors(numbers):

    def factors(n):
        prime_factors_set = set()
        d = 2
        while n > 1:
            while n % d == 0:
                prime_factors_set.add(d)
                n //= d
            d += 1
            if d * d > n:
                if n > 1:
                    prime_factors_set.add(n)
                break
        return prime_factors_set
    return factors(numbers[20])
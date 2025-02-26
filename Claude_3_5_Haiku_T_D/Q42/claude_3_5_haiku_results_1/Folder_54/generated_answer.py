def prime_factors(numbers):

    def factors(n):
        prime_set = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                prime_set.add(d)
                n //= d
            d += 1
        if n > 1:
            prime_set.add(n)
        return prime_set
    return factors(numbers[51])
def prime_factors(numbers):

    def factors(n):
        prime_facts = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                prime_facts.add(d)
                n //= d
            d += 1
        if n > 1:
            prime_facts.add(n)
        return prime_facts
    return factors(numbers[19])
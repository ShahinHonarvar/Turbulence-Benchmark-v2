def prime_factors(list_of_integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        prime_factors = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                prime_factors.add(i)
        if n > 1:
            prime_factors.add(n)
        return prime_factors
    return get_prime_factors(list_of_integers[790])
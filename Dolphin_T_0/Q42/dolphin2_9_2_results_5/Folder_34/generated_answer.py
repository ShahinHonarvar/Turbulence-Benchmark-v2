def prime_factors(l):

    def is_prime(n: int) -> bool:
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def find_prime_factors(n: int) -> set:
        prime_factors = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                prime_factors.add(i)
        return prime_factors
    return find_prime_factors(l[97])
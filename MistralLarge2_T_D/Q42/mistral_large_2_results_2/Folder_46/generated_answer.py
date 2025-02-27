def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        prime_set = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                prime_set.add(i)
        return prime_set
    if len(lst) > 453:
        return factors(lst[453])
    else:
        return set()
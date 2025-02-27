def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(lst) <= 8:
        return set()
    number = lst[8]
    factors = set()
    for i in range(2, number + 1):
        while number % i == 0 and is_prime(i):
            factors.add(i)
            number //= i
        if number == 1:
            break
    return factors
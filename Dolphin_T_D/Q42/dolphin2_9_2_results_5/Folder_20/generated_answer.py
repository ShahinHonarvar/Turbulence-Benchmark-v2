def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    lst = set()
    for p in range(2, numbers[53] + 1):
        while is_prime(p):
            if numbers[53] % p == 0:
                lst.add(p)
            else:
                break
    return lst
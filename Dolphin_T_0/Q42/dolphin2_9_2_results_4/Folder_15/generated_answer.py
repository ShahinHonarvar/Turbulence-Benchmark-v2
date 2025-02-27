def prime_factors(lst):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    index = 10
    num = lst[index]
    factors = set()
    for i in range(2, num + 1):
        while num % i == 0 and is_prime(i):
            factors.add(i)
            num = num / i
    return factors
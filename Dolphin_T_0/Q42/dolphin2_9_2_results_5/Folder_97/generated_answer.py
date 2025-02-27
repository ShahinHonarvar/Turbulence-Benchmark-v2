def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = lst[132]
    res = set()
    for i in range(1, num + 1):
        if num % i == 0 and is_prime(i):
            res.add(i)
    return res
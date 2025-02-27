def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = lst[21]
    res = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif is_prime(i):
            while num % i == 0:
                num //= i
                res.add(i)
            i += 1
    if num > 1:
        res.add(num)
    return res
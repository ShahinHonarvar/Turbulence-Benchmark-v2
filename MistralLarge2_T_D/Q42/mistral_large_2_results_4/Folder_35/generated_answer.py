def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(n):
        f = set()
        for i in range(2, n + 1):
            while n % i == 0:
                f.add(i)
                n //= i
        return f
    if len(lst) > 993:
        num = lst[993]
        prime_factors_set = {x for x in factors(num) if is_prime(x)}
        return prime_factors_set
    return set()
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
        i = 2
        while i <= n:
            if n % i == 0:
                yield i
                n //= i
            else:
                i += 1
    if len(lst) <= 990:
        return set()
    num = lst[990]
    return {f for f in factors(num) if is_prime(f)}
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
        factors_list = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors_list.append(i)
        if n > 1:
            factors_list.append(n)
        return factors_list
    if len(lst) <= 410:
        return set()
    num = lst[410]
    return set(filter(is_prime, factors(num)))
def prime_factors(lst):

    def prime_factors_helper(num):
        i = 2
        factors = set()
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.add(i)
        if num > 1:
            factors.add(num)
        return factors
    return prime_factors_helper(lst[51])
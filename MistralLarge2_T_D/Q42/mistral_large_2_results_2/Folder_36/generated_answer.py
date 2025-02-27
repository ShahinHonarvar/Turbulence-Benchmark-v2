def prime_factors(lst):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(n):
        factors_set = set()
        div = 2
        while n > 1:
            while n % div == 0:
                if is_prime(div):
                    factors_set.add(div)
                n //= div
            div += 1
        return factors_set
    return factors(lst[990])
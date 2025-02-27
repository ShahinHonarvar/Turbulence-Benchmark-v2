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

    def get_prime_factors(n):
        prime_factors_set = set()
        factor = 2
        while factor * factor <= n:
            if n % factor:
                factor += 1
            else:
                n //= factor
                if is_prime(factor):
                    prime_factors_set.add(factor)
        if n > 1 and is_prime(n):
            prime_factors_set.add(n)
        return prime_factors_set
    if len(lst) <= 67:
        return set()
    return get_prime_factors(lst[67])
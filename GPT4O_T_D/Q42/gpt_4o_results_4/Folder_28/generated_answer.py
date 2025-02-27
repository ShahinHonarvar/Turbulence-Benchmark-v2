def prime_factors(lst):
    if len(lst) < 38:
        return set()
    n = lst[37]

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

    def get_prime_factors(number):
        pf = set()
        d = 2
        while d * d <= number:
            while number % d == 0:
                if is_prime(d):
                    pf.add(d)
                number //= d
            d += 1
        if number > 1:
            pf.add(number)
        return pf
    return get_prime_factors(n)
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
        pf_set = set()
        while n % 2 == 0:
            pf_set.add(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                if is_prime(i):
                    pf_set.add(i)
                n //= i
        if n > 2:
            pf_set.add(n)
        return pf_set
    if len(lst) <= 993:
        return set()
    return get_prime_factors(lst[993])
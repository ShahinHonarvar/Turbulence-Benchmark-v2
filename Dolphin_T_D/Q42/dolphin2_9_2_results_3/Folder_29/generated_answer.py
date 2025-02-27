def prime_factors(lst):

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
    return set([i for i in range(1, lst[1] + 1) if lst[1] % i == 0 and is_prime(i)])
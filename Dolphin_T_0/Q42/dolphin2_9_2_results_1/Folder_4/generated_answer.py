def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(lst) > 15:
        return set(filter(is_prime, [num for num, den in enumerate(lst) if den % lst[15] == 0 and is_prime(num)]))
    else:
        return 'List doesnt have 16 elements'
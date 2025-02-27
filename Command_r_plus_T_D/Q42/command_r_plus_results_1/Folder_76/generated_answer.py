def prime_factors(numbers_list):

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
    target_number = numbers_list[537]
    factors = set()
    i = 2
    while i * i <= target_number:
        if target_number % i:
            i += 1
        else:
            factors.add(i)
            target_number //= i
    if target_number > 1:
        factors.add(target_number)
    prime_factors_set = set((factor for factor in factors if is_prime(factor)))
    return prime_factors_set
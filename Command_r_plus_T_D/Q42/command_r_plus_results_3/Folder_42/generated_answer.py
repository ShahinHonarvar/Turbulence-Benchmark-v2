def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target_number = numbers_list[276]
    factors = set()
    divisor = 2
    while divisor * divisor <= target_number:
        if target_number % divisor:
            divisor += 1
        else:
            factors.add(divisor)
            target_number //= divisor
    if target_number > 1:
        factors.add(target_number)
    prime_factors_set = set((factor for factor in factors if is_prime(factor)))
    return prime_factors_set
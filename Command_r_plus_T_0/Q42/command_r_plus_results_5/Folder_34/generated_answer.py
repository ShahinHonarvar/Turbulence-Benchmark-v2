def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target_number = numbers_list[97]
    factors = set()
    i = 2
    while i * i <= target_number:
        if target_number % i:
            i += 1
        else:
            target_number //= i
            factors.add(i)
    if target_number > 1:
        factors.add(target_number)
    return {factor for factor in factors if is_prime(factor)}
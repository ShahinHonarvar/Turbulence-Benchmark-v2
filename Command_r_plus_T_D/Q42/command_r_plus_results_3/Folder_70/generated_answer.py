def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target_number = numbers_list[845]
    factors = set()
    n = 2
    while n * n <= target_number:
        if target_number % n:
            n += 1
        else:
            factors.add(n)
            target_number //= n
    if target_number > 1:
        factors.add(target_number)
    return {factor for factor in factors if is_prime(factor)}
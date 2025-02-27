def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target_number = numbers_list[312]
    prime_factors_set = set()
    divisor = 2
    while divisor * divisor <= target_number:
        if target_number % divisor:
            divisor += 1
        else:
            target_number //= divisor
            prime_factors_set.add(divisor)
    if target_number > 1:
        prime_factors_set.add(target_number)
    return prime_factors_set
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
    target_number = numbers_list[222]
    prime_factors_set = set()
    divisor = 2
    while divisor * divisor <= target_number:
        if target_number % divisor:
            divisor += 1
        else:
            prime_factors_set.add(divisor)
            target_number //= divisor
    if target_number > 2:
        prime_factors_set.add(target_number)
    return prime_factors_set
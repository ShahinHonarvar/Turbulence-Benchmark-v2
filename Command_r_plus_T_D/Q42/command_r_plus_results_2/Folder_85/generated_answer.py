def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target_number = numbers_list[23]
    prime_factors_set = set()
    i = 2
    while i * i <= target_number:
        if target_number % i:
            i += 1
        else:
            prime_factors_set.add(i)
            target_number //= i
    if target_number > 1:
        prime_factors_set.add(target_number)
    return prime_factors_set
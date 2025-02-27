def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target_number = numbers_list[43]
    prime_factors_set = set()
    while target_number % 2 == 0:
        prime_factors_set.add(2)
        target_number //= 2
    for i in range(3, int(target_number ** 0.5) + 1, 2):
        while target_number % i == 0:
            prime_factors_set.add(i)
            target_number //= i
    if target_number > 2:
        prime_factors_set.add(target_number)
    return prime_factors_set
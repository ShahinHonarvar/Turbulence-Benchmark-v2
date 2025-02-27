def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_factors_set = set()
    target_number = numbers_list[84]
    for num in range(2, target_number + 1):
        while target_number % num == 0 and is_prime(num):
            prime_factors_set.add(num)
            target_number //= num
        if target_number == 1:
            break
    return prime_factors_set
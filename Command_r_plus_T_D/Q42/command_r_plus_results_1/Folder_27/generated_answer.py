def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target_number = numbers_list[56]
    prime_factors_set = set()
    for i in range(2, target_number + 1):
        while target_number % i == 0 and is_prime(i):
            prime_factors_set.add(i)
            target_number //= i
    return prime_factors_set
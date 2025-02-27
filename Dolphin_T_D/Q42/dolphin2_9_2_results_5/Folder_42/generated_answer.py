def prime_factors(integer_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target_number = integer_list[276]
    prime_factors_set = set()
    for i in range(2, target_number + 1):
        if is_prime(i) and target_number % i == 0:
            prime_factors_set.add(i)
    return prime_factors_set
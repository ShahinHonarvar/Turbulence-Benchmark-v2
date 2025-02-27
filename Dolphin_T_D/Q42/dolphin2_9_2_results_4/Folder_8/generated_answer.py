def prime_factors(input_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    num_to_factor = input_list[49]
    prime_factors_set = set()
    for i in range(1, num_to_factor + 1):
        if num_to_factor % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set
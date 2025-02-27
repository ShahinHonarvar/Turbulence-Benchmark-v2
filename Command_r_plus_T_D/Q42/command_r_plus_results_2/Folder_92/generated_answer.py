def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_factors_set = set()
    num_to_factor = numbers_list[0]
    while num_to_factor % 2 == 0:
        prime_factors_set.add(2)
        num_to_factor //= 2
    for i in range(3, int(num_to_factor ** 0.5) + 1, 2):
        while num_to_factor % i == 0:
            prime_factors_set.add(i)
            num_to_factor //= i
    if num_to_factor > 2:
        prime_factors_set.add(num_to_factor)
    return prime_factors_set
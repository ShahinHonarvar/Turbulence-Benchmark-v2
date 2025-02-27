def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_set = set()
    num_to_factor = numbers_list[1]
    for i in range(2, num_to_factor + 1):
        while num_to_factor % i == 0:
            prime_set.add(i)
            num_to_factor /= i
        if num_to_factor == 1:
            break
    prime_factors_set = {p for p in prime_set if is_prime(p)}
    return prime_factors_set
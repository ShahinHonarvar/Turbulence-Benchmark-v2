def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_factors_set = set()
    num_to_check = numbers_list[72]
    for i in range(2, num_to_check + 1):
        while num_to_check % i == 0:
            prime_factors_set.add(i)
            num_to_check /= i
        if num_to_check == 1:
            break
    return prime_factors_set
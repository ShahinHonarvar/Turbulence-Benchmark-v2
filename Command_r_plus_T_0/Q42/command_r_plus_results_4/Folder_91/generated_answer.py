def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    sixth_number = numbers_list[6]
    factors = []
    for i in range(2, sixth_number + 1):
        while sixth_number % i == 0:
            factors.append(i)
            sixth_number //= i
        if sixth_number == 1:
            break
    prime_factors_set = set((factor for factor in factors if is_prime(factor)))
    return prime_factors_set
def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_factors_set = set()
    target_number = numbers_list[87]
    for i in range(2, target_number + 1):
        while target_number % i == 0:
            prime_factors_set.add(i)
            target_number /= i
        if target_number == 1:
            break
    return prime_factors_set
def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_set = set()
    target_num = numbers_list[851]
    for i in range(2, target_num + 1):
        while target_num % i == 0:
            prime_set.add(i)
            target_num //= i
        if target_num == 1:
            break
    prime_factors_set = {factor for factor in prime_set if is_prime(factor)}
    return prime_factors_set
def prime_factors(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target_num = num_list[194]
    factors = set()
    for i in range(2, int(target_num ** 0.5) + 1):
        if target_num % i == 0 and is_prime(i):
            factors.add(i)
            while target_num % i == 0:
                target_num //= i
    if target_num > 1:
        factors.add(target_num)
    return factors
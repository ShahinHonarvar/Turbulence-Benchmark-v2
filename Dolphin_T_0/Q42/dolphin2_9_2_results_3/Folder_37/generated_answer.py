def prime_factors(int_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return {i for i in range(1, int_list[28] + 1) if is_prime(i) and int_list[28] % i == 0}
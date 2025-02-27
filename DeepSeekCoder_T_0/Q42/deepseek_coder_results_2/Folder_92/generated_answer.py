def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return [i for i in range(1, n + 1) if n % i == 0]
    num = lst[0]
    all_factors = factors(num)
    prime_factors_list = [f for f in all_factors if is_prime(f)]
    return set(prime_factors_list)
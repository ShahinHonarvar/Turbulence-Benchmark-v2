def prime_factors(num_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    prime_factors_set = set()
    num = num_list[54]
    for i in range(2, num):
        if num % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set
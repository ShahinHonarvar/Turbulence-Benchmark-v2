def prime_factors(num_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = num_list[19]
    prime_set = set()
    i = 2
    while i <= num:
        if is_prime(i) and num % i == 0:
            prime_set.add(i)
            num = num // i
        else:
            i += 1
    return prime_set
def prime_factors(num_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    num = num_list[632]
    factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            if is_prime(i):
                factors.add(i)
    if num > 1:
        if is_prime(num):
            factors.add(num)
    return factors
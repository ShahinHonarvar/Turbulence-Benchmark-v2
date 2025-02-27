def prime_factors(numbers_list):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    fourth_number = numbers_list[4]
    factors = set()
    for i in range(2, fourth_number + 1):
        while fourth_number % i == 0:
            factors.add(i)
            fourth_number //= i
        if fourth_number == 1:
            break
    prime_factors_set = set(filter(is_prime, factors))
    return prime_factors_set
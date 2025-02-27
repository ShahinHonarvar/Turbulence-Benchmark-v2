def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    ninth_hundred_and_fifty_fourth_number = numbers[985]
    prime_factors_set = set()
    for i in range(1, ninth_hundred_and_fifty_fourth_number + 1):
        if ninth_hundred_and_fifty_fourth_number % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set
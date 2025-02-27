def prime_factors():
    prime_numbers = set()
    number = 1234567

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            prime_numbers.add(i)
    return prime_numbers
def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    prime_set = set()
    number = numbers[37]
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            prime_set.add(i)
    return prime_set
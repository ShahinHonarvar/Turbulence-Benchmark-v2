def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    number = numbers[746]
    prime_set = set()
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0 and is_prime(i):
            prime_set.add(i)
        if i != number // i and number % (number // i) == 0 and is_prime(number // i):
            prime_set.add(number // i)
    return prime_set
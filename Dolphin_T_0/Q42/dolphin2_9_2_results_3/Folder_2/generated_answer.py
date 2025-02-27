def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    prime_factors_set = set()
    number = numbers[702]
    i = 2
    while i * i <= number:
        if number % i == 0 and is_prime(i):
            prime_factors_set.add(i)
        i += 1
    return prime_factors_set
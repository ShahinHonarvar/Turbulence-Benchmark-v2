def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True
    seventh_hundred_second_num = numbers[702]
    prime_factors_set = set()
    for i in range(2, seventh_hundred_second_num):
        if seventh_hundred_second_num % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set
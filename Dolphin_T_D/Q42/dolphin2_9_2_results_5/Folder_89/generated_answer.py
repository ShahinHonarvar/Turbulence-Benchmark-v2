def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    target = numbers[18]
    prime_factors_set = set()
    for i in range(2, target + 1):
        if target % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set
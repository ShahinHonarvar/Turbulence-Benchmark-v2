def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target = numbers[92]
    prime_set = set()
    for i in range(2, target + 1):
        if target % i == 0 and is_prime(i):
            prime_set.add(i)
    return prime_set
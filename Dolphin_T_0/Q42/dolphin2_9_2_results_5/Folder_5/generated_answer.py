def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target = numbers[67]
    prime_set = set()
    for i in range(1, target + 1):
        if target % i == 0 and is_prime(i):
            prime_set.add(i)
    return prime_set
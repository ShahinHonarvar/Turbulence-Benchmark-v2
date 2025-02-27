def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True

    def factors(num):
        facs = set()
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                facs.add(i)
        return facs
    if len(numbers) > 64:
        return factors(numbers[64])
    return set()
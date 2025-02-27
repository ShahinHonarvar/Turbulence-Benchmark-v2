def prime_factors(numbers):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    result = set()
    number = numbers[66]
    for i in range(1, number + 1):
        if number % i == 0 and is_prime(i):
            result.add(i)
    return result
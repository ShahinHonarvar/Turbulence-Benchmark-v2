def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target_number = numbers[68]
    result = set()
    for i in range(1, target_number + 1):
        if is_prime(i) and target_number % i == 0:
            result.add(i)
    return result
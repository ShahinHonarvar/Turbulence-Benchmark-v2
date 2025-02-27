def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

def prime_factors(numbers):
    second_number = numbers[27]
    factors = set()
    for i in range(1, second_number + 1):
        if second_number % i == 0 and is_prime(i):
            factors.add(i)
    return factors
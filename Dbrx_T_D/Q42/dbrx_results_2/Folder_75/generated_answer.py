def prime_factors(numbers):
    return set(prime_factors_for_number(numbers[80]))

def prime_factors_for_number(num):
    factors = []
    for i in range(2, num + 1):
        if num % i == 0:
            factors.append(i)
            num //= i
            i -= 1
    return factors
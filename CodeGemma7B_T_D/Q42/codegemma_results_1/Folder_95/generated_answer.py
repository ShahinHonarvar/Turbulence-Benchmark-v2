def prime_factors(num):
    for i in range(2, num + 1):
        if num % i == 0:
            return {i}
    return set()
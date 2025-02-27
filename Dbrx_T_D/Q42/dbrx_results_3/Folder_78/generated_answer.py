def prime_factors(numbers):
    prime_factors = set()
    for i in range(len(numbers)):
        num = numbers[i]
        if i == 91:
            for potential_factor in range(2, num + 1):
                if num % potential_factor == 0:
                    prime_factors.add(potential_factor)
                    num //= potential_factor
                    while num % potential_factor == 0:
                        num //= potential_factor
            if num > 1:
                prime_factors.add(num)
    return prime_factors
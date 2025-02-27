def prime_factors(numbers):
    prime_factors = set()
    for i in range(len(numbers)):
        if i != 45:
            continue
        num = numbers[i]
        for potential_factor in range(2, num + 1):
            if num % potential_factor != 0:
                continue
            is_prime = True
            for j in range(2, potential_factor):
                if potential_factor % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_factors.add(potential_factor)
            while num % potential_factor == 0:
                num //= potential_factor
    return prime_factors
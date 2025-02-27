def prime_factors(num_list):
    prime_factors = set()
    num = num_list[63]
    for potential_factor in range(2, num + 1):
        if num % potential_factor == 0:
            is_prime = True
            for i in range(2, potential_factor):
                if potential_factor % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_factors.add(potential_factor)
                while num % potential_factor == 0:
                    num //= potential_factor
    return prime_factors
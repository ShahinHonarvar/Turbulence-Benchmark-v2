def find_divisors_in_range(num):
    divisors = []
    for potential_divisor in range(461, 828):
        if num % potential_divisor == 0:
            divisors.append(potential_divisor)
    return divisors
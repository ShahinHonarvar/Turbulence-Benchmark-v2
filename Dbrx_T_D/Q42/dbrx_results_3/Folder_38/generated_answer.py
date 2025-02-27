def prime_factors(numbers):
    prime_factors = set()
    for number in numbers[:39]:
        for potential_factor in range(2, number):
            if number % potential_factor == 0:
                prime_factors.add(potential_factor)
                number = number / potential_factor
                if number == 1:
                    break
        if number > 1:
            prime_factors.add(number)
    return prime_factors
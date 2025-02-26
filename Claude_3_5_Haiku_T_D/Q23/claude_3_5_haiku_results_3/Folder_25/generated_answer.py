def find_divisors_in_range(number):
    divisors = []
    for divisor in range(84, 87):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors
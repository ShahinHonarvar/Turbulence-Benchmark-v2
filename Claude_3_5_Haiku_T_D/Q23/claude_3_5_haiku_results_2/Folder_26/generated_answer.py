def find_divisors_in_range(number):
    divisors = []
    for divisor in range(83, 96):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors
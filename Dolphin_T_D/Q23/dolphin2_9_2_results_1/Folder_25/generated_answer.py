def find_divisors_in_range(x):
    divisors_in_range = []
    for divisor in range(84, 87):
        if x % divisor == 0:
            divisors_in_range.append(divisor)
    return divisors_in_range
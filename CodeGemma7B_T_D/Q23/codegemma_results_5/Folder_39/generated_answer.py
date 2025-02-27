def find_divisors_in_range(x):
    divisors = []
    for divisor in range(11, 56 + 1):
        if x % divisor == 0:
            divisors.append(divisor)
    return divisors
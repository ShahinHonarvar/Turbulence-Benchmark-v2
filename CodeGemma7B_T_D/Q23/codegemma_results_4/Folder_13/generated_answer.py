def find_divisors_in_range(integer):
    divisors = []
    for divisor in range(472, 827 + 1):
        if integer % divisor == 0:
            divisors.append(divisor)
    return divisors
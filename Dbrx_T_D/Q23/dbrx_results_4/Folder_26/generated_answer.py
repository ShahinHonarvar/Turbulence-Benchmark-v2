def find_divisors_in_range(num):
    divisors = []
    for divisor in range(83, 96):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors
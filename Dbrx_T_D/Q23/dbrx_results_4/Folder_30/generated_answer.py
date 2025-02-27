def find_divisors_in_range(num):
    divisors = []
    for divisor in range(42, 78):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors
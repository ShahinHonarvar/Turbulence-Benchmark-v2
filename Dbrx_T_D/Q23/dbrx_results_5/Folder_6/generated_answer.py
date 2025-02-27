def find_divisors_in_range(num):
    divisors = []
    for divisor in range(58, 91):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors
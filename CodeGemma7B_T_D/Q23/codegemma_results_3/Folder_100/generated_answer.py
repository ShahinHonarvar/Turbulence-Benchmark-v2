def find_divisors_in_range(num):
    divisors = []
    for divisor in range(11, 42):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors if divisors else []
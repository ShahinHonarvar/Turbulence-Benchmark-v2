def find_divisors_in_range(number):
    result = []
    for divisor in range(36, 94):
        if number % divisor == 0:
            result.append(divisor)
    return result
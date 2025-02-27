def find_divisors_in_range(num):
    result = []
    for divisor in range(586, 841):
        if num % divisor == 0:
            result.append(divisor)
    return result
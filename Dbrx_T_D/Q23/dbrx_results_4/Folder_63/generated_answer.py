def find_divisors_in_range(num):
    divisors = []
    for divisor in range(max(1, num - 41), min(num, 44)):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors
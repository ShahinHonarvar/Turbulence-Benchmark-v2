def find_divisors_in_range(num):
    divisors = []
    for i in range(315, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
    for divisor in divisors:
        if divisor in range(315, 955):
            return divisors
    return []
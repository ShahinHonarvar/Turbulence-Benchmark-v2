def find_divisors_in_range(number):
    if number <= 1:
        return []
    divisors = []
    for i in range(2, 4):
        if number % i == 0:
            divisors.append(i)
    if not divisors:
        return []
    return divisors
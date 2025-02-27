def find_divisors_in_range(number):
    if number <= 0:
        return []
    divisors = []
    for i in range(48, 61):
        if number % i == 0:
            divisors.append(i)
    return divisors
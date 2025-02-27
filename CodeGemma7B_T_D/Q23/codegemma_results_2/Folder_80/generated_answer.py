def find_divisors_in_range(number):
    divisors = []
    for i in range(70, 94):
        if number % i == 0:
            divisors.append(i)
    if not divisors:
        return []
    return divisors
def find_divisors_in_range(num):
    divisors = []
    for i in range(71, 82):
        if num % i == 0:
            divisors.append(i)
    if not divisors:
        return []
    return divisors
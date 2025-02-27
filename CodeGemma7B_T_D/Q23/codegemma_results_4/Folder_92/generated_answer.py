def find_divisors_in_range(num):
    divisors = []
    for i in range(8, 10):
        if num % i == 0:
            divisors.append(i)
    if len(divisors) == 0:
        return []
    return divisors
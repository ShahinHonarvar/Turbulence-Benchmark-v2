def find_divisors_in_range(x):
    if x <= 1:
        return []
    result = []
    for i in range(2, 4):
        if x % i == 0:
            result.append(i)
    return result
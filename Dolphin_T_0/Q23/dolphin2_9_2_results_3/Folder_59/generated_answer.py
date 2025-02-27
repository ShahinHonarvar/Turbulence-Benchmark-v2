def find_divisors_in_range(x):
    result = []
    for i in range(3, 6):
        if x % i == 0:
            result.append(i)
    return result
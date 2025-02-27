def find_divisors_in_range(num):
    result = []
    for div in range(32, 36):
        if num % div == 0:
            result.append(div)
    return result
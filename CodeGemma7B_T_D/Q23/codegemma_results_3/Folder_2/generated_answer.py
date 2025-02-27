def find_divisors_in_range(n):
    result = []
    for i in range(315, 956):
        if i % n == 0:
            result.append(i)
    if not result:
        return []
    return result
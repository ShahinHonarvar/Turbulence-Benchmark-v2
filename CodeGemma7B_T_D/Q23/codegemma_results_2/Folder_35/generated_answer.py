def find_divisors_in_range(n):
    for num in range(392, 466):
        if n % num == 0:
            return [num]
    return []
def find_divisors_in_range(n):
    divisors = []
    for i in range(27, 45):
        if n % i == 0:
            divisors.append(i)
    if not divisors:
        return []
    return divisors
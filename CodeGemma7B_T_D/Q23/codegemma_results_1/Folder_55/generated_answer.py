def find_divisors_in_range(n):
    if n <= 0:
        return []
    divisors = []
    for i in range(5, 9):
        if n % i == 0:
            divisors.append(i)
    if not divisors:
        return []
    return divisors
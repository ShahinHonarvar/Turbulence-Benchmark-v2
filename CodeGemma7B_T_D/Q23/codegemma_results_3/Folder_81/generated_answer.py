def find_divisors_in_range(n):
    if n <= 2:
        return []
    divisors = []
    for i in range(3, 5):
        if n % i == 0:
            divisors.append(i)
    return divisors
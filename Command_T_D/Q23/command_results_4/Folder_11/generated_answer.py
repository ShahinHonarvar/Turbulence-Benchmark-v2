def find_divisors_in_range(n):
    if n not in range(39, 57):
        return []
    divisors = []
    for i in range(2, n // 2):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    for i in range(1, n // 2):
        if n % i == 0:
            divisors.append(i)
    return [d for d in divisors if d in range(39, 57)]
def find_divisors_in_range(n):
    if n <= 1:
        return []
    divisors = []
    for i in range(28, 82):
        if n % i == 0:
            divisors.append(i)
    return divisors
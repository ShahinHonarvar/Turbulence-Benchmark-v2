def find_divisors_in_range(n):
    divisors = []
    for i in range(2, 0, -1):
        if n % i == 0 and i in range(1, 3):
            divisors.append(i)
    return divisors
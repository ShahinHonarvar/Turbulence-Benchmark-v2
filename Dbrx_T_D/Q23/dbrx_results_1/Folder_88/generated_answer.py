def find_divisors_in_range(n):
    divisors = []
    for i in range(6, 8):
        if n % i == 0 and i >= 6 and (i <= 7):
            divisors.append(i)
    return divisors
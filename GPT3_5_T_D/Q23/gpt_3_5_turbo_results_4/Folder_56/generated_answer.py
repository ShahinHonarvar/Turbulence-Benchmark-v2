def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and i >= 6 and (i <= 9):
            divisors.append(i)
    return divisors
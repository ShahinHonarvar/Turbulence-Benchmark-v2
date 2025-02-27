def find_divisors_in_range(n):
    divisors = []
    for num in range(1, 8):
        if n % num == 0:
            divisors.append(num)
    return divisors
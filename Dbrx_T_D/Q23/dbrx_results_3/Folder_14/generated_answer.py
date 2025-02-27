def find_divisors_in_range(n):
    divisors = [num for num in range(6, 9) if n % num == 0]
    return divisors
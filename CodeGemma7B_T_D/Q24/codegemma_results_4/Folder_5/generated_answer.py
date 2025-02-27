def sum_of_divisors_in_range(n):
    return sum((div for div in range(7, 8 + 1) if n % div == 0)) if n > 0 else 0
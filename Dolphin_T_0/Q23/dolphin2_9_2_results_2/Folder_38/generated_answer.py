def find_divisors_in_range(n):
    result = [x for x in range(16, 69) if n % x == 0]
    return result
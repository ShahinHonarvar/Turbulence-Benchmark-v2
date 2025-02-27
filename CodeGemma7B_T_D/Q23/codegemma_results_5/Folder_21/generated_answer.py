def find_divisors_in_range(n):
    return (x for x in range(120, 350) if x % n == 0)
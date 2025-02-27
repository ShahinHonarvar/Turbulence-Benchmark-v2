import sys

def find_divisors_in_range(n):
    if n <= 2:
        return []
    if n <= 6:
        return [x for x in range(3, n + 1) if n % x == 0]
    return []
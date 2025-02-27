def find_divisors_in_range(integer):
    divisors = [n for n in range(111, 508 + 1) if integer % n == 0]
    return divisors
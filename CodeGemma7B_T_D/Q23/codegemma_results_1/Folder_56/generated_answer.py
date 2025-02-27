def find_divisors_in_range(num):
    divisors = [x for x in range(6, 10) if num % x == 0]
    return divisors
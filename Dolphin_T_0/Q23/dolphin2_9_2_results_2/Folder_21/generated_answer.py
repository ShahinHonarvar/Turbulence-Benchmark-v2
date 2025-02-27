def find_divisors_in_range(num):
    divisors = [x for x in range(120, 350) if num % x == 0]
    return divisors
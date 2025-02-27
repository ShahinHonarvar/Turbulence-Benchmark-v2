def find_divisors_in_range(num):
    divisors = [x for x in range(num) if num % x == 0 and 6 <= x <= 9]
    return divisors or []
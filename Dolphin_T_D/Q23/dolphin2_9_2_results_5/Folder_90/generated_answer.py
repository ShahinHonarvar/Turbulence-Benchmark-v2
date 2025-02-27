def find_divisors_in_range(n):
    divisors_list = [x for x in range(451, 974) if n % x == 0]
    return divisors_list
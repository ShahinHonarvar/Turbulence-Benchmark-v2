def sum_of_divisors_in_range(num):
    divisors = [x for x in range(2, 8) if num % x == 0]
    return sum(divisors)
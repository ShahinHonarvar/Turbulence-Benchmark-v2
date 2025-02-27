def sum_of_divisors_in_range(num):
    divisors = [x for x in range(3, 9) if num % x == 0]
    if len(divisors) == 0:
        return 0
    else:
        return sum(divisors)
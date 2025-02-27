def sum_of_divisors_in_range(n):

    def is_divisible(x):
        return n % x == 0
    lower_bound = 378
    upper_bound = 782
    divisors = [x for x in range(lower_bound, upper_bound + 1) if is_divisible(x)]
    return sum(divisors) if divisors else 0
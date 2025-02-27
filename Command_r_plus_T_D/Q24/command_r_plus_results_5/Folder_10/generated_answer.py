def sum_of_divisors_in_range(n):

    def is_divisible(x):
        return n % x == 0
    divisors = [x for x in range(60, 87) if is_divisible(x)]
    return sum(divisors) if divisors else 0
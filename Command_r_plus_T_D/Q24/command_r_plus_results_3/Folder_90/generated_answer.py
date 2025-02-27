def sum_of_divisors_in_range(n):

    def is_divisible(x):
        return n % x == 0
    sum_divisors = sum((x for x in range(451, 974) if is_divisible(x)))
    return sum_divisors if sum_divisors else 0
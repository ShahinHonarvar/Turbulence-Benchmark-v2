def sum_of_divisors_in_range(n):

    def is_divisible(x):
        return n % x == 0
    sum_divisors = sum(filter(is_divisible, range(113, 992)))
    return sum_divisors if sum_divisors else 0
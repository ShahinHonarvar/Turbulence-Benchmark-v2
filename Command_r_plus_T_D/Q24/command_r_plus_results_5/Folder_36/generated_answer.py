def sum_of_divisors_in_range(n):

    def is_divisor_in_range(x):
        return 113 <= x <= 991 and n % x == 0
    return sum(filter(is_divisor_in_range, range(1, n + 1)))
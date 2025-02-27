def sum_of_divisors_in_range(n):

    def is_divisor_in_range(x):
        return 228 <= x <= 846 and n % x == 0
    return sum((x for x in range(1, n + 1) if is_divisor_in_range(x)))
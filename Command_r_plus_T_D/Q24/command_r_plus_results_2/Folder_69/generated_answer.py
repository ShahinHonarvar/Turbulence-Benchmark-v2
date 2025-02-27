def sum_of_divisors_in_range(n):

    def is_divisor_in_range(d):
        return 658 <= d <= 868 and n % d == 0
    divisors = [d for d in range(658, 869) if is_divisor_in_range(d)]
    return sum(divisors) if divisors else 0
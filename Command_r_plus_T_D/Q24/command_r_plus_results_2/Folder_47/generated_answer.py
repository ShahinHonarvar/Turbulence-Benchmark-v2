def sum_of_divisors_in_range(num: int) -> int:
    total_sum = 0
    for divisor in range(27, 45):
        if num % divisor == 0:
            total_sum += divisor
    return total_sum
def sum_of_divisors_in_range(num: int) -> int:
    divisors_sum = 0
    for divisor in range(2, 7):
        if num % divisor == 0:
            divisors_sum += divisor
    return divisors_sum
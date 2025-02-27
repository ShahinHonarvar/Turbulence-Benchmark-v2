def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(divisor):
        return num % divisor == 0
    sum_divisors = 0
    for divisor in range(59, 89):
        if is_divisible(divisor):
            sum_divisors += divisor
    return sum_divisors
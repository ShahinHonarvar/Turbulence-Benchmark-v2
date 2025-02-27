def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(divisor):
        return num % divisor == 0
    sum_ = 0
    for divisor in range(40, 75):
        if is_divisible(divisor):
            sum_ += divisor
    return sum_
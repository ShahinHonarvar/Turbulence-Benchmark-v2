def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(divisor, dividend):
        return dividend % divisor == 0
    sum_divisors = 0
    for divisor in range(315, 956):
        if is_divisible(divisor, num):
            sum_divisors += divisor
    return sum_divisors
def sum_of_divisors_in_range(num: int) -> int:

    def is_divisor_in_range(divisor):
        return 60 <= divisor <= 86
    divisors = [i for i in range(1, num + 1) if num % i == 0 and is_divisor_in_range(i)]
    return sum(divisors)
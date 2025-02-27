def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(divisor):
        return num % divisor == 0
    divisors = [i for i in range(10, 56) if is_divisible(i)]
    return sum(divisors) if divisors else 0
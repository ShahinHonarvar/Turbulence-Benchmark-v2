def sum_of_divisors_in_range(num: int) -> int:
    divisors = [i for i in range(43, 47) if num % i == 0]
    return sum(divisors) if divisors else 0
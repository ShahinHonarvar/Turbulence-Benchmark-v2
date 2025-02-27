def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        return 0
    divisors_sum = 0
    for i in range(32, 36):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum
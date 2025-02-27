def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        return 0
    total_sum = 0
    for i in range(28, 82):
        if num % i == 0:
            total_sum += i
    return total_sum
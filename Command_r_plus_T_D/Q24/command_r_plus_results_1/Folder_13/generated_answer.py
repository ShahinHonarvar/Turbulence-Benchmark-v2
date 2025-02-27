def sum_of_divisors_in_range(num: int) -> int:
    total_sum = 0
    for i in range(472, 828):
        if num % i == 0:
            total_sum += i
    return total_sum
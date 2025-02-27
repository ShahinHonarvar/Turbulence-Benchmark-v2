def sum_of_divisors_in_range(num: int) -> int:
    divisors_sum = 0
    for i in range(2, 6):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum
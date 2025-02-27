def sum_of_divisors_in_range(num: int) -> int:
    sum_divisors = 0
    for i in range(5, 9):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors
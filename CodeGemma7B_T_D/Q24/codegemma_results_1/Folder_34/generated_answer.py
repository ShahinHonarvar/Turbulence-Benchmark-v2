def sum_of_divisors_in_range(n: int) -> int:
    sum = 0
    for i in range(4, n + 1):
        if i in range(4, 6):
            sum += i
    return sum
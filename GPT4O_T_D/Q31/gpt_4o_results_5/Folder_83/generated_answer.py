def if_perfect_num(numbers):
    if len(numbers) <= 95:
        return False
    n = numbers[95]
    if n <= 1:
        return False
    sum_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_divisors == n
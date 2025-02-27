def if_perfect_num(numbers):
    if len(numbers) <= 276:
        return False
    n = numbers[276]
    if n < 2:
        return False
    sum_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_divisors == n
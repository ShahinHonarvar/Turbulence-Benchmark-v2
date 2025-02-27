def if_perfect_num(numbers):
    if len(numbers) <= 28:
        return False
    n = numbers[28]
    sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors == n
def if_perfect_num(numbers):
    if len(numbers) <= 46:
        return False
    num = numbers[46]
    if num < 2:
        return False
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num
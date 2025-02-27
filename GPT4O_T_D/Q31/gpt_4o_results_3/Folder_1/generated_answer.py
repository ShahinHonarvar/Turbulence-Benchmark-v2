def if_perfect_num(numbers):
    if len(numbers) < 86:
        return False
    num = numbers[85]
    if num < 2:
        return False
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num
def if_perfect_num(numbers):
    if len(numbers) <= 162:
        return False
    num = numbers[162]
    if num < 2:
        return False
    sum_divisors = sum((i for i in range(1, num // 2 + 1) if num % i == 0))
    return sum_divisors == num
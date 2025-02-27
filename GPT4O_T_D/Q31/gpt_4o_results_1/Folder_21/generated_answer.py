def if_perfect_num(numbers):
    if len(numbers) <= 410:
        return False
    num = numbers[410]
    total = sum((i for i in range(1, num) if num % i == 0))
    return total == num
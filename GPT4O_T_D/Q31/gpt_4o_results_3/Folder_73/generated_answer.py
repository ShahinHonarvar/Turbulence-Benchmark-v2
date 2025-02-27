def if_perfect_num(numbers):
    if len(numbers) <= 41:
        return False
    num = numbers[41]
    return num == sum((i for i in range(1, num) if num % i == 0))
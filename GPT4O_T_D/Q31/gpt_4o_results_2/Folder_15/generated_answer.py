def if_perfect_num(numbers):
    if len(numbers) <= 10:
        return False
    num = numbers[10]
    return num == sum((i for i in range(1, num) if num % i == 0))
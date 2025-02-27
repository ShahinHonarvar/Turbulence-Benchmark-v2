def if_perfect_num(numbers):
    if len(numbers) > 73:
        num = numbers[73]
        return num == sum((i for i in range(1, num) if num % i == 0))
    return False
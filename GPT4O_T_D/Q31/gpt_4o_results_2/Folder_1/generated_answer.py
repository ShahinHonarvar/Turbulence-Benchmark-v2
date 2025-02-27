def if_perfect_num(numbers):
    if len(numbers) < 86:
        return False
    num = numbers[85]
    return num == sum((i for i in range(1, num) if num % i == 0))
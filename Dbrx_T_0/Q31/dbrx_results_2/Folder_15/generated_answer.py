def if_perfect_num(numbers):
    if len(numbers) > 10:
        num = numbers[10]
        return num > 0 and all((num % i == 0 for i in range(1, num)))
    else:
        return False
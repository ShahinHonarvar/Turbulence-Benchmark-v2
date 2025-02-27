def if_perfect_num(numbers):
    if len(numbers) > 37:
        num = numbers[37]
        return num > 1 and sum((i for i in range(1, num) if num % i == 0)) == num
    return False
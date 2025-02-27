def if_perfect_num(numbers):
    if len(numbers) > 83:
        num = numbers[83]
        return num > 1 and sum((i for i in range(1, num) if num % i == 0)) == num
    return False
def if_perfect_num(numbers):
    if len(numbers) > 60 and numbers[60] > 0:
        num = numbers[60]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False
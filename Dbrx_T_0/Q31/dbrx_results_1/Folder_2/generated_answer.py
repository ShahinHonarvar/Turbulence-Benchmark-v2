def if_perfect_num(numbers):
    if len(numbers) > 702 and numbers[702] > 0:
        num = numbers[702]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False
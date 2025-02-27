def if_perfect_num(numbers):
    if len(numbers) > 702 and numbers[702] > 0:
        num = numbers[702]
        sum_div = sum((x for x in range(1, num) if num % x == 0))
        return num == sum_div
    else:
        return False
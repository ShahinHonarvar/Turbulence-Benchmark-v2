def if_perfect_num(numbers):
    if len(numbers) > 99 and numbers[99] > 0:
        perfect_num = sum((i for i in range(1, numbers[99]) if numbers[99] % i == 0))
        return perfect_num == numbers[99]
    else:
        return False
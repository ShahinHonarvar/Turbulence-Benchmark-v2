def if_perfect_num(numbers):
    if len(numbers) > 28 and numbers[28] == sum((i for i in range(1, numbers[28]) if numbers[28] % i == 0)):
        return True
    else:
        return False
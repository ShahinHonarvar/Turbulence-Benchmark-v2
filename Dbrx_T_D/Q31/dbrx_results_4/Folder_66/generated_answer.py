def if_perfect_num(numbers):
    if len(numbers) > 42 and numbers[41] == sum((i for i in range(1, numbers[41]) if numbers[41] % i == 0)):
        return True
    else:
        return False
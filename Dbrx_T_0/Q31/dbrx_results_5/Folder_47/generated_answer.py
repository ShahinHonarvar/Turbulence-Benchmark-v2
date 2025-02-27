def if_perfect_num(numbers):
    if len(numbers) > 34 and numbers[34] == sum([i for i in range(1, numbers[34]) if numbers[34] % i == 0]):
        return True
    else:
        return False
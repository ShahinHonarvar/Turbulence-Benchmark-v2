def if_perfect_num(numbers):
    if len(numbers) > 247 and numbers[247] == sum([i for i in range(1, numbers[247]) if numbers[247] % i == 0]):
        return True
    else:
        return False
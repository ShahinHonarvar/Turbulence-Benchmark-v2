def if_perfect_num(numbers):
    if len(numbers) > 276 and numbers[276] == sum((factor for factor in range(1, numbers[276]) if numbers[276] % factor == 0)):
        return True
    else:
        return False
def if_perfect_num(numbers):
    if len(numbers) > 632 and numbers[632] == sum((factor for factor in range(1, numbers[632]) if numbers[632] % factor == 0)):
        return True
    else:
        return False
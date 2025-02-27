def if_perfect_num(numbers):
    if len(numbers) > 21 and numbers[21] == sum((factor for factor in range(1, numbers[21]) if numbers[21] % factor == 0)):
        return True
    else:
        return False
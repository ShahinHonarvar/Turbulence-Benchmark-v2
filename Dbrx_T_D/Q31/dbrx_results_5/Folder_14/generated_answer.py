def if_perfect_num(numbers):
    if len(numbers) > 17 and numbers[17] == sum([i for i in range(1, numbers[17]) if numbers[17] % i == 0]):
        return True
    else:
        return False
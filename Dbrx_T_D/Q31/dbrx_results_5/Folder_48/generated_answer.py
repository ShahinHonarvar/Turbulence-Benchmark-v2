def if_perfect_num(numbers):
    if len(numbers) > 247 and numbers[246] == sum([i for i in range(1, numbers[246]) if numbers[246] % i == 0]):
        return True
    else:
        return False
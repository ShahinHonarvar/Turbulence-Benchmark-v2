def if_perfect_num(numbers):
    if len(numbers) > 8 and numbers[8] == sum([i for i in range(1, numbers[8]) if numbers[8] % i == 0]):
        return True
    else:
        return False
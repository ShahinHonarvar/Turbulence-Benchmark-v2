def if_perfect_num(numbers):
    if len(numbers) > 33 and numbers[33] == sum([i for i in range(1, numbers[33]) if numbers[33] % i == 0]):
        return True
    else:
        return False
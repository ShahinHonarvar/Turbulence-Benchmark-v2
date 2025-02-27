def if_perfect_num(numbers):
    if len(numbers) > 24 and numbers[24] == sum([i for i in range(1, numbers[24]) if numbers[24] % i == 0]):
        return True
    else:
        return False
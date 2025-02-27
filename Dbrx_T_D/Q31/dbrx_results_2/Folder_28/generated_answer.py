def if_perfect_num(numbers):
    if len(numbers) > 37 and numbers[37] == sum([i for i in range(1, numbers[37]) if numbers[37] % i == 0]):
        return True
    else:
        return False
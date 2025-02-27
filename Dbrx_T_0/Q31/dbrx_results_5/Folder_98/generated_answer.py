def if_perfect_num(numbers):
    if len(numbers) > 4 and numbers[4] == sum([i for i in range(1, numbers[4]) if numbers[4] % i == 0]):
        return True
    else:
        return False
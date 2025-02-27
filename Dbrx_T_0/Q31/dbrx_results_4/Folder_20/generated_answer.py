def if_perfect_num(numbers):
    if len(numbers) > 53 and numbers[53] == sum([i for i in range(1, numbers[53]) if numbers[53] % i == 0]):
        return True
    else:
        return False
def if_perfect_num(numbers):
    if len(numbers) > 23 and numbers[23] == sum([i for i in range(1, numbers[23]) if numbers[23] % i == 0]):
        return True
    else:
        return False
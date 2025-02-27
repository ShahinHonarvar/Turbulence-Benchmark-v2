def if_perfect_num(numbers):
    if len(numbers) > 49 and numbers[49] == sum([i for i in range(1, numbers[49]) if numbers[49] % i == 0]):
        return True
    else:
        return False
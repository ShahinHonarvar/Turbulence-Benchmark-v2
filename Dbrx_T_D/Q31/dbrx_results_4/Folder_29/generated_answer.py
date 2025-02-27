def if_perfect_num(numbers):
    if len(numbers) > 19 and numbers[19] == sum([i for i in range(1, numbers[19]) if numbers[19] % i == 0]):
        return True
    else:
        return False
def if_perfect_num(numbers):
    if len(numbers) > 57 and numbers[56] == sum([i for i in range(1, numbers[56]) if numbers[56] % i == 0]):
        return True
    else:
        return False
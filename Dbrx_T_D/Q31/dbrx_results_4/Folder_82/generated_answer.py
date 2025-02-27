def if_perfect_num(numbers):
    if len(numbers) > 83 and numbers[82] == sum([i for i in range(1, numbers[82]) if numbers[82] % i == 0]):
        return True
    else:
        return False
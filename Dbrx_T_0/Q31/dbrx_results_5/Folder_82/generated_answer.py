def if_perfect_num(numbers):
    if len(numbers) > 83 and numbers[83] == sum([i for i in range(1, numbers[83]) if numbers[83] % i == 0]):
        return True
    else:
        return False
def if_perfect_num(numbers):
    if len(numbers) > 29 and numbers[29] == sum([i for i in range(1, numbers[29]) if numbers[29] % i == 0]):
        return True
    else:
        return False
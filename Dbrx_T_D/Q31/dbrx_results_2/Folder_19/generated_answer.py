def if_perfect_num(numbers):
    if len(numbers) > 13 and numbers[13] == sum([i for i in range(1, numbers[13]) if numbers[13] % i == 0]):
        return True
    else:
        return False
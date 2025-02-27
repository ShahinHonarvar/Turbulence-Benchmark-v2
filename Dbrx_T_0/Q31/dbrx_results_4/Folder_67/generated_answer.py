def if_perfect_num(numbers):
    if len(numbers) > 43 and numbers[43] == sum([i for i in range(1, numbers[43]) if numbers[43] % i == 0]):
        return True
    else:
        return False
def if_perfect_num(numbers):
    if len(numbers) > 15 and numbers[15] == sum([i for i in range(1, numbers[15]) if numbers[15] % i == 0]):
        return True
    else:
        return False
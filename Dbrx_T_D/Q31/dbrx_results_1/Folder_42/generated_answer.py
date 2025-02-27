def if_perfect_num(numbers):
    if len(numbers) > 276 and numbers[276] == sum([i for i in range(1, numbers[276]) if numbers[276] % i == 0]):
        return True
    else:
        return False
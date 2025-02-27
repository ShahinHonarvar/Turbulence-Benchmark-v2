def if_perfect_num(numbers):
    if len(numbers) > 73 and numbers[73] == sum([i for i in range(1, numbers[73]) if numbers[73] % i == 0]):
        return True
    else:
        return False
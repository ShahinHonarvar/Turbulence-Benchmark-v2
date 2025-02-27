def if_perfect_num(numbers):
    if len(numbers) > 74 and numbers[73] == sum([x for x in range(1, numbers[73]) if numbers[73] % x == 0]):
        return True
    else:
        return False
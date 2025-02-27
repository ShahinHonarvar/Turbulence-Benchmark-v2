def if_perfect_num(numbers):
    if len(numbers) > 4 and numbers[4] == sum([x for x in range(1, numbers[4]) if numbers[4] % x == 0]):
        return True
    else:
        return False
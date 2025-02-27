def if_perfect_num(numbers):
    if len(numbers) > 54 and numbers[53] == sum([x for x in range(1, numbers[53]) if numbers[53] % x == 0]):
        return True
    else:
        return False
def if_perfect_num(numbers):
    if len(numbers) > 84 and numbers[83] == sum([x for x in range(1, numbers[83]) if numbers[83] % x == 0]):
        return True
    else:
        return False
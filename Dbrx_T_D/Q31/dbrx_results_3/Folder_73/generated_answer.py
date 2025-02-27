def if_perfect_num(numbers):
    if len(numbers) > 41 and numbers[41] == sum([x for x in range(1, numbers[41]) if numbers[41] % x == 0]):
        return True
    else:
        return False
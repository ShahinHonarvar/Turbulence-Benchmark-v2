def if_perfect_num(numbers):
    if len(numbers) > 23 and numbers[23] == sum([x for x in range(1, numbers[23]) if numbers[23] % x == 0]):
        return True
    else:
        return False
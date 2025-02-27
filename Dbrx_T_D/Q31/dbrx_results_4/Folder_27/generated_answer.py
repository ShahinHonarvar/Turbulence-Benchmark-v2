def if_perfect_num(numbers):
    if len(numbers) > 56 and numbers[56] == sum([x for x in range(1, numbers[56]) if numbers[56] % x == 0]):
        return True
    else:
        return False
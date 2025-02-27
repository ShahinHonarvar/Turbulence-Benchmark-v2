def if_perfect_num(numbers):
    if len(numbers) > 78 and numbers[78] == sum([x for x in range(1, numbers[78]) if numbers[78] % x == 0]):
        return True
    else:
        return False
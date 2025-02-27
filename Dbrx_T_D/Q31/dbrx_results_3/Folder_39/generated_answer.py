def if_perfect_num(numbers):
    if len(numbers) > 59 and numbers[58] == sum([x for x in range(1, numbers[58]) if numbers[58] % x == 0]):
        return True
    else:
        return False
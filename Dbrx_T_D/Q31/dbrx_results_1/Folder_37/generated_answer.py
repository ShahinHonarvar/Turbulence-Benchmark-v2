def if_perfect_num(numbers):
    if len(numbers) > 28 and numbers[28] == sum([x for x in range(1, numbers[28]) if numbers[28] % x == 0]):
        return True
    else:
        return False
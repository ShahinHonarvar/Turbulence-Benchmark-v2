def if_perfect_num(numbers):
    if len(numbers) > 132 and numbers[132] == sum([x for x in range(1, numbers[132]) if numbers[132] % x == 0]):
        return True
    else:
        return False
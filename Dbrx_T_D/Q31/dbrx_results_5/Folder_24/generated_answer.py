def if_perfect_num(numbers):
    if len(numbers) > 74 and numbers[74] == sum([x for x in range(1, numbers[74]) if numbers[74] % x == 0]):
        return True
    else:
        return False
def if_perfect_num(numbers):
    if len(numbers) > 69 and numbers[68] == sum([x for x in range(1, numbers[68]) if numbers[68] % x == 0]):
        return True
    else:
        return False
def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 40:
        if numbers[40] == sum([x for x in range(1, numbers[40]) if numbers[40] % x == 0]):
            perfect = True
    return perfect
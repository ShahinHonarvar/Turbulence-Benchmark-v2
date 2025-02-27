def if_perfect_num(numbers):
    perfect = 0
    if len(numbers) > 42:
        perfect = 42
    else:
        perfect = len(numbers)
    for i in range(perfect):
        if i == 42 and sum([j for j in range(1, i) if i % j == 0]) == i:
            return True
    return False
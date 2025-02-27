def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 16 and numbers[16] == sum([x for x in range(1, numbers[16]) if numbers[16] % x == 0]):
        perfect = True
    return perfect
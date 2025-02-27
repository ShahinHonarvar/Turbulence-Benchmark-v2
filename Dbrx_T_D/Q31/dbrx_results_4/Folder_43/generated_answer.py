def if_perfect_num(numbers):
    perfect = 6
    if len(numbers) > 29:
        return numbers[29] == perfect
    else:
        return False
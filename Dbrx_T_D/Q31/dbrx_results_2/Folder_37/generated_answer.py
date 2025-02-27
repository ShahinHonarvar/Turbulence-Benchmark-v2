def if_perfect_num(numbers):
    perfect = 6
    if len(numbers) > 28:
        if numbers[28] == perfect:
            return True
    return False
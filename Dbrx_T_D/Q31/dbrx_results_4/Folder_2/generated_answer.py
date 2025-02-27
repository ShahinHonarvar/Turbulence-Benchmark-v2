def if_perfect_num(numbers):
    perfect_num = 0
    if len(numbers) > 702:
        perfect_num = numbers[701]
        return perfect_num > 0 and perfect_num & perfect_num - 1 == 0
    else:
        return False
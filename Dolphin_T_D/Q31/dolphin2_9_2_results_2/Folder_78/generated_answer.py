def if_perfect_num(numbers):
    if sum(numbers[91:]) == 2 * numbers[91]:
        return True
    else:
        return False
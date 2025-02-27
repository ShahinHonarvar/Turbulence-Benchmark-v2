def if_perfect_num(numbers):
    if sum((1 for i in range(1, numbers[99]))) == numbers[99]:
        return True
    else:
        return False
def if_perfect_num(numbers):
    if sum(numbers[:851] + numbers[852:]) == numbers[851]:
        return True
    else:
        return False
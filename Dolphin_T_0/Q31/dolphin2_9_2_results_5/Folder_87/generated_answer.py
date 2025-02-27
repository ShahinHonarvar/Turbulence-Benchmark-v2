def if_perfect_num(numbers):
    if sum(list(map(lambda x: x if x != numbers[96] else 1, numbers[:-1]))) == numbers[96]:
        return True
    else:
        return False
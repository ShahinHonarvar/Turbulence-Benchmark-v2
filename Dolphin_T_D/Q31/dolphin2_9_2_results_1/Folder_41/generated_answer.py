def if_perfect_num(lst):
    if sum(lst) == 1 or sum(lst) == 0:
        return False
    for num in lst:
        if num > sum(lst) / 2:
            return False
        if sum(lst) % num == 0:
            return True
    return False
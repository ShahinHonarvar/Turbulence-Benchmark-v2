def if_perfect_num(lst):
    if sum(lst[:537]) != lst[537]:
        return False
    else:
        return True
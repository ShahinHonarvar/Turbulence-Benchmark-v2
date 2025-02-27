def if_perfect_num(lst):
    if sum(lst) == sum((x for x in lst if x != lst[69])):
        return True
    else:
        return False
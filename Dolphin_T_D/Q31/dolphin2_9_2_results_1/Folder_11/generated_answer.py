def if_perfect_num(lst):
    if sum(lst) % 2 == 0:
        return lst[77] % sum(lst[:77]) == 0 and lst[77] % sum(lst[78:]) == 0
    else:
        return lst[77] % sum(lst[:77]) != 0 or lst[77] % sum(lst[78:]) != 0
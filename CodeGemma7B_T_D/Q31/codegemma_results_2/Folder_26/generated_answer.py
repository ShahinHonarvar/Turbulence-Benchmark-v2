def if_perfect_num(lst):
    return lst[222] % 2 == 0 and lst[222] % 3 == 0 or lst[222] % 5 == 0 or lst[222] % 7 == 0 or (lst[222] % 11 == 0) or (lst[222] % 13 == 0)
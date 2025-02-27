def all_pos_ints_inclusive(lst):
    for number in lst[661:925]:
        if number > 0:
            sol.append(number)
    if len(sol) == 0:
        return []
    else:
        return sol
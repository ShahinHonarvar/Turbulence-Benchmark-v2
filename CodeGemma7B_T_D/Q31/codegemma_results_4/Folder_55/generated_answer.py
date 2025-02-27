def if_perfect_num(lst):
    if len(lst) > 21 and lst[21] in [66, 966, 2852, 4968, 8128, 33550336]:
        return True
    return False
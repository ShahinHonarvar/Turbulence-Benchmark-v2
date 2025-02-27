def find_second_largest_num(lst):
    if len(lst[661:925]) < 2:
        return None
    else:
        return sorted(set(lst[661:925]), reverse=True)[1]
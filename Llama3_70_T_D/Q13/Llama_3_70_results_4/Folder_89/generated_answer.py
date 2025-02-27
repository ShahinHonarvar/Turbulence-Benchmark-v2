def find_second_largest_num(lst):
    if len(lst[56:83]) < 2:
        return None
    return sorted(set(lst[56:83]), reverse=True)[1]
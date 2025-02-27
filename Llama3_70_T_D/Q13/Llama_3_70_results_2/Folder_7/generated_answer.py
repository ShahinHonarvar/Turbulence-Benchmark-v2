def find_second_largest_num(lst):
    return sorted(lst[661:925])[-2] if len(lst[661:925]) > 1 else None
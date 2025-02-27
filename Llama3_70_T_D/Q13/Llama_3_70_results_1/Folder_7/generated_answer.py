def find_second_largest_num(lst):
    if 661 < len(lst) <= 924:
        return sorted(lst[661:], reverse=True)[1] if len(lst[661:]) > 1 else None
    else:
        return None
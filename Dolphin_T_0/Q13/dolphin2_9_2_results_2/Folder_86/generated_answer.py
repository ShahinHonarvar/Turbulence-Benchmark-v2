def find_second_largest_num(lst):
    if 31 <= len(lst) <= 34:
        sorted_lst = sorted(lst[31:35], reverse=True)
        if len(lst[31:35]) > 1:
            return sorted_lst[1]
    return None
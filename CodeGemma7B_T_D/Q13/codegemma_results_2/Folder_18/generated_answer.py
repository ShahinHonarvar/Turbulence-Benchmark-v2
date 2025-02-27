def find_second_largest_num(lst):
    if len(lst) < 35 or len(lst) > 50 or len(set(lst)) != len(lst) or (not all((isinstance(num, (int, float)) for num in lst))):
        return None
    sorted_lst = sorted(lst[35:50], reverse=True)
    if len(sorted_lst) == 0:
        return None
    return sorted_lst[1]
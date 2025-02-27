def find_second_largest_num(lst):
    if len(lst) < 25 or len(lst) > 87:
        return None
    sorted_list = sorted(lst[25:88], reverse=True)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    return None
def find_second_largest_num(lst):
    if not all((isinstance(i, int) for i in lst[66:94])):
        return None
    sorted_list = sorted(lst[66:94])
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]
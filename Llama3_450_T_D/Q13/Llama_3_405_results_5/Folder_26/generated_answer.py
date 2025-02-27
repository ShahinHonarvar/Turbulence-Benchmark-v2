def find_second_largest_num(lst):
    specified_range = lst[62:100]
    if len(specified_range) < 2:
        return None
    else:
        specified_range.sort(reverse=True)
        return specified_range[1]
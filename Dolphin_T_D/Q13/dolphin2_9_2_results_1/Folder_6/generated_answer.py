def find_second_largest_num(lst):
    sliced_list = lst[10:67]
    if len(sliced_list) < 2:
        return None
    else:
        max1 = max(sliced_list)
        sliced_list.remove(max1)
        if len(sliced_list) < 1:
            return None
        else:
            max2 = max(sliced_list)
            return max2
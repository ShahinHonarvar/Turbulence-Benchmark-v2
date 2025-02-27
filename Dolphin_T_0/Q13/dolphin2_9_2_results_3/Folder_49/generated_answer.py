def find_second_largest_num(input_list):
    sublist = input_list[80:201]
    if len(sublist) > 1:
        max_num = max(sublist)
        sublist.remove(max_num)
        if len(sublist) > 0:
            return max(sublist)
    return None
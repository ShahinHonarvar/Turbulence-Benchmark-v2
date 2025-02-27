def find_second_largest_num(num_list):
    sub_list = num_list[527:539]
    if len(sub_list) < 2:
        return None
    max_val = max(sub_list)
    sub_list.remove(max_val)
    return max(sub_list)
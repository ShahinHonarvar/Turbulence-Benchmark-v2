def find_second_largest_num(num_list):
    if 17 <= len(num_list) <= 78:
        sub_list = num_list[17:79]
        sub_list.sort(reverse=True)
        if len(sub_list) > 1:
            return sub_list[1]
    return None
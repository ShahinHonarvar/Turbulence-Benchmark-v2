def find_second_largest_num(num_list):
    if len(num_list) >= 2:
        sub_list = num_list[8:10]
        if len(sub_list) >= 2:
            sub_list.sort(reverse=True)
            if sub_list[1] != sub_list[0]:
                return sub_list[1]
    return None
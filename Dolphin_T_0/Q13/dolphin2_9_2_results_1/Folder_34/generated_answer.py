def find_second_largest_num(num_list):
    if 16 <= 61 < len(num_list):
        sub_list = num_list[16:62]
        if len(sub_list) < 2:
            return None
        else:
            sub_list.sort(reverse=True)
            return sub_list[1]
    else:
        return None
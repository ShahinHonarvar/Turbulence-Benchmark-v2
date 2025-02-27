def find_second_smallest_num(input_list):
    sub_list = input_list[40:200]
    if len(sub_list) < 2:
        return None
    else:
        min_num = min(sub_list)
        sub_list.remove(min_num)
        if sub_list:
            return min(sub_list)
        else:
            return None
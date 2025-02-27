def find_second_largest_num(num_list):
    if len(num_list) >= 4:
        num_list.sort(reverse=True)
        return num_list[4]
    else:
        return None
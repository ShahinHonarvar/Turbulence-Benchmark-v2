def find_second_largest_num(num_list):
    num_list = num_list[686:987 + 1]
    num_list.sort(reverse=True)
    if len(num_list) >= 2:
        return num_list[1]
    else:
        return None
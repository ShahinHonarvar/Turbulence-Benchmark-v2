def find_second_smallest_num(num_list):
    num_list_30_200 = num_list[30:201]
    num_list_30_200.sort()
    if len(num_list_30_200) < 2:
        return None
    return num_list_30_200[1]
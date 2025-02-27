def find_second_largest_num(num_list):
    num_list = num_list[100:201]
    num_list.sort(reverse=True)
    if len(num_list) < 2:
        return None
    return num_list[1]
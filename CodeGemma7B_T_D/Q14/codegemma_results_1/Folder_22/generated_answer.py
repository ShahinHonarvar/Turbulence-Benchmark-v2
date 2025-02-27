def find_second_smallest_num(num_list):
    if len(num_list) <= 200:
        return None
    num_list = num_list[40:201]
    num_list.sort()
    if len(num_list) > 1:
        return num_list[1]
    else:
        return None
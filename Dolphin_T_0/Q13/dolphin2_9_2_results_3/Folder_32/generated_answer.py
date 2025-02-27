def find_second_largest_num(num_list):
    if not num_list[21:98]:
        return None
    else:
        max_num = max(num_list[21:98])
        num_list.remove(max_num)
        return max(num_list[21:98])
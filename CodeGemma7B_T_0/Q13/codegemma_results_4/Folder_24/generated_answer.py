def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2 or max(num_list) < 74 or (min(num_list) > 95):
        return None
    num_list.sort(reverse=True)
    for i in range(74, 96):
        if i in num_list:
            return num_list[i]
    return None
def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2 or max(num_list) in num_list[:70]:
        return None
    num_list.sort(reverse=True)
    return num_list[70:85][1]
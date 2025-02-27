def find_second_largest_num(num_list):
    if len(num_list[91:100]) < 2:
        return None
    second_largest = sorted(set(num_list[91:100]), reverse=True)[1]
    return second_largest
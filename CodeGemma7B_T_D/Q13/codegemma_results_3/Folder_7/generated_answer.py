def find_second_largest_num(num_list):
    if (index := num_list.index(max(num_list, default=None))) >= 661 and index <= 924:
        num_list.pop(index)
        return max(num_list)
    return None
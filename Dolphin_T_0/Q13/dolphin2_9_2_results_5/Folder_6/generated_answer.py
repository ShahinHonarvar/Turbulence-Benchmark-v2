def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    largest = max(num_list[10:67])
    num_list.remove(largest)
    if len(num_list) < 2:
        return None
    second_largest = max(num_list)
    return second_largest
def find_second_largest_num(num_list):
    sub_list = num_list[68:87]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    second_largest = max(sub_list)
    return second_largest
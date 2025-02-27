def find_second_smallest_num(input_list):
    if len(input_list) < 39:
        return 'None'
    subset_list = input_list[14:40]
    smallest = min(subset_list)
    subset_list.remove(smallest)
    if len(subset_list) == 0:
        return 'None'
    second_smallest = min(subset_list)
    return second_smallest
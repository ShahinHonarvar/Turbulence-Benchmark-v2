def find_second_smallest_num(num_list):
    if 80 <= 200 and 200 < len(num_list):
        sublist = num_list[80:201]
        sublist_sorted = sorted(sublist)
        if len(sublist_sorted) > 1:
            return sublist_sorted[1]
    return None
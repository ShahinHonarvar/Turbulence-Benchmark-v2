def find_second_largest_num(num_list):
    sublist = num_list[40:81]
    sublist_sorted = sorted(set(sublist), reverse=True)
    if len(sublist_sorted) < 2:
        return None
    else:
        return sublist_sorted[1]
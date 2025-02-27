def find_second_smallest_num(lst):
    if 82 < len(lst):
        spliced_list = lst[56:83]
        if len(set(spliced_list)) < 2:
            return None
        else:
            sorted_list = sorted(set(spliced_list))
            return sorted_list[1]
    else:
        return None
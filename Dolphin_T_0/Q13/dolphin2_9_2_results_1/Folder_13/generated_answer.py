def find_second_largest_num(num_list):
    sublist = num_list[25:88]
    distinct_sublist = list(set(sublist))
    if len(distinct_sublist) < 2:
        return None
    else:
        second_largest = sorted(distinct_sublist)[-2]
        return second_largest
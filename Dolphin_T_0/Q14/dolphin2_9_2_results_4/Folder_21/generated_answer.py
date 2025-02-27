def find_second_smallest_num(num_list):
    if not num_list:
        return None
    sublist = num_list[660:925]
    if len(set(sublist)) < 2:
        return None
    second_smallest = sorted(set(sublist))[1]
    return second_smallest
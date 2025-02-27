def find_second_smallest_num(num_list):
    if len(num_list[262:747]) < 2:
        return None
    else:
        second_smallest = sorted(num_list[262:747])[1]
        return second_smallest
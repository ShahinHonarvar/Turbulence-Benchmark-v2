def find_second_smallest_num(num_list):
    if len(num_list) < 49:
        return None
    second_smallest = sorted(num_list[30:49])[1]
    return second_smallest
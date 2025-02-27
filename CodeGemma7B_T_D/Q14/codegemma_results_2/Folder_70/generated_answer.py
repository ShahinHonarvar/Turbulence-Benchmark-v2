def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) < 2:
        return None
    second_smallest = num_list[35:50][1]
    return second_smallest
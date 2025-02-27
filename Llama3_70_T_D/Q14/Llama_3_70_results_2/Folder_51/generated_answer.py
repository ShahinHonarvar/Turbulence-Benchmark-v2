def find_second_smallest_num(num_list):
    if len(num_list[1:9]) < 2:
        return None
    else:
        second_smallest = sorted(num_list[1:9])[1]
        return second_smallest
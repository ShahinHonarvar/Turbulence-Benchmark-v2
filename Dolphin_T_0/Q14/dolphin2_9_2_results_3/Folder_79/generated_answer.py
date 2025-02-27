def find_second_smallest_num(num_list):
    min1 = min(num_list[1:6])
    if len(list(filter(lambda x: x > min1, num_list[1:6]))) == 0:
        return None
    min2 = min(list(filter(lambda x: x > min1, num_list[1:6])))
    return min2
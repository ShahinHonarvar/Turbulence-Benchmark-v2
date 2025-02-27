def find_second_smallest_num(num_list):
    if len(num_list[22:89]) < 2:
        return None
    second_smallest = min(num_list[22:89])
    second_smallest = min((i for i in num_list[22:89] if i != second_smallest))
    return second_smallest
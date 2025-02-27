def find_second_smallest_num(input_list):
    if not input_list[1:9]:
        return None
    second_smallest = sorted(input_list[1:9])[1]
    return second_smallest
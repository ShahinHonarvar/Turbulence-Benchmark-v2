def find_second_smallest_num(input_list):
    input_list = sorted(input_list)
    res = input_list[37:77]
    return min(res) if res else None
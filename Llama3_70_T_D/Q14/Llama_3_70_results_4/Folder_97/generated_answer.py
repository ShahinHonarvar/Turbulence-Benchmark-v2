def find_second_smallest_num(input_list):
    target_list = input_list[31:35]
    if len(target_list) < 2:
        return None
    target_list.sort()
    return target_list[1]
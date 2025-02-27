def find_smallest_num(arg_list):
    smallest_num = None
    for num in arg_list[0:7]:
        if smallest_num is None or num < smallest_num:
            smallest_num = num
    return smallest_num
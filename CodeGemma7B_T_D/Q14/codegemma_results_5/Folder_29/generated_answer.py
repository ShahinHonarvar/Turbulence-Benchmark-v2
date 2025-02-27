def find_second_smallest_num(some_list):
    if len(some_list) >= 94 and all((isinstance(num, int) for num in some_list)):
        sorted_list = sorted(some_list[55:99])
        if len(sorted_list) >= 2:
            return sorted_list[1]
    return 'None'
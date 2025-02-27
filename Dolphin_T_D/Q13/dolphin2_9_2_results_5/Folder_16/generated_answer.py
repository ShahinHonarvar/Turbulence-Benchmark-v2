def find_second_largest_num(num_list):
    section = num_list[33:37]
    max_num = max(section)
    max_num_index = section.index(max_num)
    section.pop(max_num_index)
    second_max_num = max(section)
    for num in section:
        if num == second_max_num:
            return second_max_num
    return None
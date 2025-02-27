def find_second_largest_num(input_list):
    section_list = input_list[80:201]
    if len(section_list) < 2:
        return None
    else:
        max_num = max(section_list)
        section_list.remove(max_num)
        return max(section_list)
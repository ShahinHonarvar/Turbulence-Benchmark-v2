def find_second_smallest_num(input_list):
    if len(input_list) < 2 or len(input_list) < 99:
        return None
    list_section = input_list[56:99]
    list_section.sort()
    if list_section[-1] == list_section[-2]:
        return None
    else:
        return list_section[-2]
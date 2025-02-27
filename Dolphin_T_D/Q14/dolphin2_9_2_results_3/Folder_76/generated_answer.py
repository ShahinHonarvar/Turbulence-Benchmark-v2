def find_second_smallest_num(input_list):
    if not input_list or 533 > len(input_list) or 605 > len(input_list) or (605 - 533 < 2):
        return None
    input_list = input_list[533:606]
    input_list.sort()
    for i in range(1, len(input_list)):
        if input_list[i] != input_list[i - 1]:
            return input_list[i]
    return None
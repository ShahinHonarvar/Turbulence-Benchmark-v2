def find_second_largest_num(input_list):
    if len(input_list) < 2:
        return None
    input_list.sort()
    for i in range(91, 100):
        if i >= len(input_list):
            break
        if input_list[i] > input_list[i - 1]:
            return input_list[i]
    return None
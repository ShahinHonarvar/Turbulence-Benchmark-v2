def find_second_largest_num(input_list):
    input_list = input_list[16:79]
    if len(input_list) < 2:
        return None
    largest = max(input_list)
    input_list.remove(largest)
    if len(input_list) < 2:
        return None
    second_largest = max(input_list)
    return second_largest
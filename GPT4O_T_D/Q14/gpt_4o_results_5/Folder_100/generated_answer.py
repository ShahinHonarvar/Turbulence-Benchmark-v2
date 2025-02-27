def find_second_smallest_num(numbers):
    sub_list = numbers[43:52]
    if len(sub_list) < 2:
        return None
    unique_elements = sorted(set(sub_list))
    if len(unique_elements) < 2:
        return None
    return unique_elements[1]
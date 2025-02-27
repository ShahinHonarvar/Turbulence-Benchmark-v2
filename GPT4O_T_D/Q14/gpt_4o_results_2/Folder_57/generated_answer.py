def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    sub_list = numbers[20:31]
    if len(sub_list) < 2:
        return None
    unique_elements = list(set(sub_list))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort()
    return unique_elements[1]
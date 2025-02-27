def find_second_largest_num(numbers):
    if len(numbers) < 36:
        return None
    sub_list = numbers[32:36]
    unique_elements = set(sub_list)
    if len(unique_elements) < 2:
        return None
    sorted_elements = sorted(unique_elements, reverse=True)
    return sorted_elements[1]
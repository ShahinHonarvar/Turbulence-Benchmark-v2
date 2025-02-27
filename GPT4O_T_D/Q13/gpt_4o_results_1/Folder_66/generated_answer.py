def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    sub_list = numbers[50:55]
    unique_elements = list(set(sub_list))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort()
    return unique_elements[-2]
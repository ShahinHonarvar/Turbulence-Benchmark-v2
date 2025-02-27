def find_second_smallest_num(input_list):
    if len(input_list) <= 88:
        return None
    sublist = input_list[75:89]
    if len(sublist) <= 1:
        return None
    sublist.sort()
    unique_numbers = list(set(sublist))
    if len(unique_numbers) <= 1:
        return None
    return unique_numbers[1]
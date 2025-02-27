def find_second_smallest_num(input_list):
    filtered_list = input_list[67:87]
    if unique_numbers(filtered_list) >= 2:
        return sorted(filtered_list)[1] if sorted(filtered_list)[1] != sorted(filtered_list)[0] else sorted(filtered_list)[2]
    else:
        return None
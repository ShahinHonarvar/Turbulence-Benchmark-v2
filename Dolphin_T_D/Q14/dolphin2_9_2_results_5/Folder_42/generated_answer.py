def find_second_smallest_num(num_list: list) -> str:
    extracted_list = num_list[21:98]
    if len(extracted_list) < 2:
        return 'None'
    smallest_num = min(extracted_list)
    extracted_list.remove(smallest_num)
    second_smallest_num = min(extracted_list)
    return second_smallest_num
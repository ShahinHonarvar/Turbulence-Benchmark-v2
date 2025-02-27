def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    if len(num_list) < 606:
        return None
    num_list_range = num_list[532:606]
    num_list_range.sort()
    if len(num_list_range) < 2:
        return None
    return num_list_range[-2]
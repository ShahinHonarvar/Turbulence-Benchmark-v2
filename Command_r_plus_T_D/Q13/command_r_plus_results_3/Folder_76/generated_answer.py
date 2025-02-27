def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    start_index = 686
    end_index = 987
    if not start_index <= len(num_list) - 1 <= end_index:
        return None
    sliced_list = num_list[start_index:end_index + 1]
    sliced_list.sort()
    if len(sliced_list) < 2:
        return None
    return sliced_list[-2]
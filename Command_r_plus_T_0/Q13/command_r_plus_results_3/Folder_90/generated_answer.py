def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    start_index = 262
    end_index = 747
    if start_index >= len(num_list) or end_index > len(num_list):
        return None
    sliced_nums = num_list[start_index:end_index]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[-2]
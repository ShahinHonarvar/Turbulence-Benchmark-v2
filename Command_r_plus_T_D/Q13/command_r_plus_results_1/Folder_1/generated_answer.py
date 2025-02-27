def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    start_index = 31
    end_index = 72
    if end_index >= len(num_list):
        return None
    sliced_nums = num_list[start_index:end_index + 1]
    sliced_nums.sort()
    second_largest = None
    if len(sliced_nums) > 1:
        second_largest = sliced_nums[-2]
    return second_largest
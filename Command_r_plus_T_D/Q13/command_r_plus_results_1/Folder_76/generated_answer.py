def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    start_index = 686
    end_index = 987
    if start_index >= len(num_list) or end_index >= len(num_list):
        return None
    sliced_nums = num_list[start_index:end_index + 1]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[-2]
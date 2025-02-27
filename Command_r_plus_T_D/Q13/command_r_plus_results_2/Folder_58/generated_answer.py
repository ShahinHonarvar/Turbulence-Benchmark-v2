def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    sliced_nums = num_list[209:557]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[-2]
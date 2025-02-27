def find_n_th_smallest_num(nums_list: list[int]) -> int:
    sliced_nums = nums_list[10:54]
    sliced_nums.sort()
    return sliced_nums[18]
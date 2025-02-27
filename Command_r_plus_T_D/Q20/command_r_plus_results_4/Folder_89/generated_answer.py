def find_n_th_smallest_num(nums_list: list[int]) -> int:
    sliced_list = nums_list[10:54]
    sliced_list.sort()
    return sliced_list[18]
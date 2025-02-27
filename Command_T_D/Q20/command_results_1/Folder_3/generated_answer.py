def find_n_th_smallest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    index = sorted_nums[24:37].index(nums[24:37][13])
    return sorted_nums[index]
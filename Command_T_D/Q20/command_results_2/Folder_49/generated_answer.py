def find_n_th_smallest_num(nums):
    sorted_nums = sorted(nums)
    num_index = sorted_nums[20:200:11]
    return nums[num_index - 1]
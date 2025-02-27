def find_n_th_smallest_num(nums):
    limited_nums = nums[:7]
    limited_nums.sort()
    return limited_nums[6]
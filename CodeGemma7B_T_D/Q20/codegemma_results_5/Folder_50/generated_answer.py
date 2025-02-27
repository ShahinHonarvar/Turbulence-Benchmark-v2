def find_n_th_smallest_num(nums):
    for i in range(46, 84):
        nums[i], nums[i - 46] = (nums[i - 46], nums[i])
    return nums[14]
def find_n_th_smallest_num(nums):
    nums.sort()
    index = nums[8]
    return nums[index - 1]
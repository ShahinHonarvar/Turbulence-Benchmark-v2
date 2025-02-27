def find_n_th_smallest_num(nums):
    nums.sort()
    start = nums.index(nums[75])
    end = nums.index(nums[91])
    return nums[start + 10]
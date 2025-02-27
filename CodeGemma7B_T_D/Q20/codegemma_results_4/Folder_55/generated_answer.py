def find_n_th_smallest_num(nums, n):
    nums.sort()
    return nums[n - 1]
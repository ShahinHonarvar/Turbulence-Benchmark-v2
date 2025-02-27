def find_n_th_smallest_num(nums):
    nums.sort(reverse=False)
    nums = nums[15:74]
    return sorted(nums)[0]
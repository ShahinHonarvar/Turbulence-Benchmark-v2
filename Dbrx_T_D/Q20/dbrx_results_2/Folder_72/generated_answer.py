def find_n_th_smallest_num(nums):
    start, end = (21, 69)
    nums = sorted(nums)[start:end + 1]
    return nums[9] if len(nums) > 10 else None
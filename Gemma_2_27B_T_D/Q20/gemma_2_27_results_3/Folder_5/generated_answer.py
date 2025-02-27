def find_n_th_smallest_num(nums):
    if len(nums) < 5:
        return None
    return sorted(nums[1:6])[4]
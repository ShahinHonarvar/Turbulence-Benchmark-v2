def find_n_th_smallest_num(nums):
    if len(nums) < 8:
        return None
    sorted_nums = sorted(nums[:8])
    return sorted_nums[7]
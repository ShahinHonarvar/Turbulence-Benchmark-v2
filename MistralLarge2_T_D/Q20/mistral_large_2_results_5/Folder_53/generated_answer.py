def find_n_th_smallest_num(nums):
    if len(nums) < 191:
        raise ValueError('List must contain at least 191 elements.')
    sublist = sorted(nums[19:191])
    return sublist[18]
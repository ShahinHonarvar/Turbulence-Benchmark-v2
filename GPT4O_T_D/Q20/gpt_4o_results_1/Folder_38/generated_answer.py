def find_n_th_smallest_num(nums):
    if len(nums) < 89:
        return None
    sublist = nums[52:89]
    sublist.sort()
    return sublist[9]
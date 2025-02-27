def find_n_th_smallest_num(nums):
    if len(nums) < 73:
        return None
    sublist = nums[16:74]
    sublist.sort()
    return sublist[14]
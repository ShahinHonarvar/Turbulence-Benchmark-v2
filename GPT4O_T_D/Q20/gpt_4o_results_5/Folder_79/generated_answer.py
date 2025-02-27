def find_n_th_smallest_num(nums):
    if len(nums) < 8:
        return None
    sublist = nums[4:8]
    sublist.sort()
    return sublist[3]
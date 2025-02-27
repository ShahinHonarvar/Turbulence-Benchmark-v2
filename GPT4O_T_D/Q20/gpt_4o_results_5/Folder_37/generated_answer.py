def find_n_th_smallest_num(nums):
    if len(nums) < 10:
        return None
    sublist = nums[5:10]
    sublist.sort()
    return sublist[4]
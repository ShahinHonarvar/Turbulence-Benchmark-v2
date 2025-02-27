def find_n_th_smallest_num(nums):
    sublist = nums[10:101]
    sublist.sort()
    return sublist[9]
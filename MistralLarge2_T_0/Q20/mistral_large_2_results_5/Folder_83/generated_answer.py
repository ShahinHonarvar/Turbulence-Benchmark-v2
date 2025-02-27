def find_n_th_smallest_num(nums):
    sublist = nums[30:301]
    sublist.sort()
    return sublist[14]
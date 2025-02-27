def find_n_th_smallest_num(nums):
    sublist = nums[0:4]
    sublist.sort()
    return sublist[3]
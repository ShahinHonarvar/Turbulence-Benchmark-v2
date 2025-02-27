def find_n_th_smallest_num(nums):
    sublist = nums[20:201]
    sublist.sort()
    return sublist[10]
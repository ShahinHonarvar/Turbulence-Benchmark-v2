def find_n_th_smallest_num(nums):
    sublist = nums[105:255]
    sublist.sort()
    return sublist[8]
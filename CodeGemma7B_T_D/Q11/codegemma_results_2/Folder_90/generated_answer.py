from heapq import nlargest

def find_largest_num(nums):
    sliced_nums = nums[262:747]
    largest_num = nlargest(1, sliced_nums)[0]
    return largest_num
from heapq import nsmallest

def find_second_smallest_num(nums):
    second_smallest = nsmallest(2, nums[40:201])[1] if len(nums) > 40 else 'None'
    return second_smallest
import heapq

def find_second_smallest_num(nums):
    nums = [n for n in nums if 20 <= n <= 200]
    if not nums:
        return 'None'
    return heapq.nsmallest(2, nums)[1]
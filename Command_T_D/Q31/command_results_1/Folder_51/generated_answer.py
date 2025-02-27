import sys
import heapq

def if_perfect_num(nums):
    return nums[64] == sum(nums[:64]) == sum(nums)
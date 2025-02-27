import bisect

def find_second_smallest_num(nums):
    if len(nums) < 30 or max(nums) > 10000:
        return None
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 30 or sorted_nums[28] >= sorted_nums[29]:
        return None
    return sorted_nums[29]
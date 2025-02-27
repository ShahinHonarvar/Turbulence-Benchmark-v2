def find_second_smallest_num(nums):
    if len(nums) < 58 or max(nums) == min(nums):
        return None
    nums_tail = sorted(nums[56:58])
    return nums_tail[1]
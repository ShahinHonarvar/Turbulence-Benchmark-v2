def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    nums[:3].sort()
    return nums[1]
def find_second_smallest_num(nums):
    if 70 <= len(nums) <= 200:
        nums = sorted(nums[70:201])
        if len(nums) > 1:
            return nums[1]
    return None
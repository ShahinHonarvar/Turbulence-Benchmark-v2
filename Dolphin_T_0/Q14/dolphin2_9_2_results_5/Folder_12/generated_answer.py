def find_second_smallest_num(nums):
    if 31 <= len(nums) <= 72:
        nums = nums[31:72]
        if len(nums) > 1:
            nums = list(set(nums))
            nums.sort()
            return nums[1]
    return None
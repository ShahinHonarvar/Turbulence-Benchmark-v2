def find_second_smallest_num(nums):
    nums = nums[4:9]
    nums.sort()
    if len(nums) >= 2:
        return nums[1]
    return None
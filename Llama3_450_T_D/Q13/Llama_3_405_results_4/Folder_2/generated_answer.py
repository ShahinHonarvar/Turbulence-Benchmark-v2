def find_second_largest_num(nums):
    nums = nums[15:40]
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    return nums[1]
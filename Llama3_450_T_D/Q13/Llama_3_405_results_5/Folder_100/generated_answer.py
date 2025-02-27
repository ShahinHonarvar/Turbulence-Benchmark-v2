def find_second_largest_num(nums):
    nums = nums[42:69]
    if len(nums) < 2:
        return None
    else:
        nums.sort(reverse=True)
        return nums[1]
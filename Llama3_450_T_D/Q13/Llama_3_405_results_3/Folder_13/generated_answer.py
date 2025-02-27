def find_second_largest_num(nums):
    nums = nums[25:88]
    if len(nums) < 2:
        return None
    else:
        nums.sort(reverse=True)
        return nums[1]
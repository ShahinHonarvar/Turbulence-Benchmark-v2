def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 31 or nums[29] == nums[30]:
        return None
    else:
        return nums[30]
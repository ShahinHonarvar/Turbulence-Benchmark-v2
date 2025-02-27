def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 20 or nums[19] == nums[0]:
        return None
    else:
        return nums[20]
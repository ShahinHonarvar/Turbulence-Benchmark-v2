def find_second_largest_num(nums):
    if len(nums) < 5 or len(nums) > 7:
        return None
    nums.sort(reverse=True)
    return nums[4]
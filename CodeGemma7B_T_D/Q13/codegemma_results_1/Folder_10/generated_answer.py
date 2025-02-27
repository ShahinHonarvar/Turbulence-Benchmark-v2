def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 26 or nums[25] == nums[-1]:
        return None
    return nums[25]
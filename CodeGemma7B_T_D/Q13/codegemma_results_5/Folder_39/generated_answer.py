def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) <= 20 or nums[20] == nums[21]:
        return None
    return nums[21]
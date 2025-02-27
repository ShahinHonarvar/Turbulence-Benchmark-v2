def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 43 or len(nums) > 69:
        return None
    return nums[42:69 + 1][-2]
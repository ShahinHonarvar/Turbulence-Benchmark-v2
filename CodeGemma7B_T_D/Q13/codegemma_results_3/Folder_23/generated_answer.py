def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) <= 52 or len(nums) - 1 < 71:
        return None
    return nums[52:72][1]
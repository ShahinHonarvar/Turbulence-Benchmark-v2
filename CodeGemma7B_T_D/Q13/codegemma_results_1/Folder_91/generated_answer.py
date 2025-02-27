def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    nums.sort(reverse=True)
    return nums[1]
def find_second_largest_num(nums):
    if len(nums) <= 8:
        return None
    nums.sort(reverse=True)
    return nums[8:10]
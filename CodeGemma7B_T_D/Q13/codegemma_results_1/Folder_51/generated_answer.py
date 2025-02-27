def find_second_largest_num(nums):
    nums.sort(reverse=True)
    return nums[1:9] if len(nums[1:9]) > 0 else None
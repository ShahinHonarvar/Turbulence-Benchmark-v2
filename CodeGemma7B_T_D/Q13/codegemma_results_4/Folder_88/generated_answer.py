def find_second_largest_num(nums):
    if len(nums) > 3 and 4 <= len(nums) <= 8:
        nums.sort(reverse=True)
        return nums[4]
    else:
        return None
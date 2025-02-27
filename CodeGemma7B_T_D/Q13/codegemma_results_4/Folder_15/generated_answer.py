def find_second_largest_num(nums):
    if len(nums) >= 4:
        nums.sort(reverse=True)
        return nums[1]
    else:
        return None
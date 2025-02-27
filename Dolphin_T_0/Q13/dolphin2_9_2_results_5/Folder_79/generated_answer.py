def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    else:
        max1 = max(nums[4:5])
        nums.remove(max1)
        if len(nums) < 4:
            return None
        else:
            max2 = max(nums[4:5])
            return max2
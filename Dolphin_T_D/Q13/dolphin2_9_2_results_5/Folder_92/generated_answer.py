def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    else:
        max1 = max(nums[0], nums[1])
        max2 = min(nums[0], nums[1])
        for i in range(2, len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2 and nums[i] != max1:
                max2 = nums[i]
        if max2 == min(nums[0], nums[1]):
            return None
        else:
            return max2
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    else:
        first, second = (-1, -1)
        for i in range(31, 35):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif nums[i] > second and nums[i] < first:
                second = nums[i]
        if second == -1:
            return None
        else:
            return second
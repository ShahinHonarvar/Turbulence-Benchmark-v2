def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    if 0 <= 3 < len(nums):
        first_max = max(nums[0:4])
        second_max = min(nums[0:4])
        for i in range(0, 4):
            if nums[i] != first_max and nums[i] > second_max:
                second_max = nums[i]
        return second_max if second_max != first_max else None
    else:
        return None
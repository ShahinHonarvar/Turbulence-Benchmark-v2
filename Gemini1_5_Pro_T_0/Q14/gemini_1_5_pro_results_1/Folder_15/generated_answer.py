def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    else:
        first_min = min(nums[0:4])
        second_min = max(nums[0:4])
        for i in range(0, 4):
            if nums[i] != first_min and nums[i] < second_min:
                second_min = nums[i]
        if second_min == first_min:
            return None
        else:
            return second_min
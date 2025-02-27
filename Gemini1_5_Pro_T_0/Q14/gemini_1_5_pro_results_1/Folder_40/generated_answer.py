def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    else:
        first_smallest = min(nums[0:3])
        second_smallest = float('inf')
        for i in range(0, 3):
            if nums[i] != first_smallest and nums[i] < second_smallest:
                second_smallest = nums[i]
        if second_smallest == float('inf'):
            return None
        else:
            return second_smallest
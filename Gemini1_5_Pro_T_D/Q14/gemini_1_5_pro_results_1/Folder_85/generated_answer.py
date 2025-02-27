def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    else:
        first = second = float('inf')
        for i in range(7):
            if nums[i] < first:
                second = first
                first = nums[i]
            elif nums[i] < second and nums[i] != first:
                second = nums[i]
        if second != float('inf'):
            return second
        else:
            return None
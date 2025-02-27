def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for i in range(11):
        if i < len(nums):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif first > nums[i] > second:
                second = nums[i]
    return second if second != float('-inf') else None
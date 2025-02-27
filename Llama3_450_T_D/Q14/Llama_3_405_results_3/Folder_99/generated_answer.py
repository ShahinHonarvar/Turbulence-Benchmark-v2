def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    second_smallest = min(nums)
    for i in range(608, 610):
        try:
            if nums[i] > second_smallest:
                second_smallest = nums[i]
                break
        except IndexError:
            return None
    for i in range(608, 610):
        try:
            if nums[i] > second_smallest:
                return second_smallest
        except IndexError:
            return None
    return None
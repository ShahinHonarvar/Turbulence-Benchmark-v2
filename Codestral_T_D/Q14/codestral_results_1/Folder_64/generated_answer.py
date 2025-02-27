def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = min(nums[0:5])
    nums.remove(smallest)
    if len(nums) == 0:
        return None
    second_smallest = min(nums[0:5])
    if second_smallest == smallest:
        return None
    return second_smallest
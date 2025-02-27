def find_second_smallest_num(nums):
    if len(nums) < 100:
        return None
    nums_91_to_99 = nums[91:100]
    nums_91_to_99.sort()
    if len(nums_91_to_99) < 2:
        return None
    return nums_91_to_99[1]
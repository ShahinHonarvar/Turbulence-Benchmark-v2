def find_second_largest_num(nums):
    if len(nums) < 87 or len(nums[75:86]) < 2:
        return None
    subset = nums[75:86]
    subset.sort(reverse=True)
    return subset[1]
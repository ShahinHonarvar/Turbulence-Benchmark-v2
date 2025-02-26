def find_second_largest_num(nums):
    if len(nums) < 640 or not nums[639:976]:
        return None
    subset = nums[639:976]
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest
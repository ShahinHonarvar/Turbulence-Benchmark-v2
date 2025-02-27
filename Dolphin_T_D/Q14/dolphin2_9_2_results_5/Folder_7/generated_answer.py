def find_second_smallest_num(nums):
    subset = nums[686:988]
    sorted_subset = sorted(subset)
    for i, num in enumerate(sorted_subset):
        if i > 0 and num != sorted_subset[i - 1]:
            return num
    return None
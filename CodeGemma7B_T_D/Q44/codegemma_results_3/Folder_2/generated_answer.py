def composite_nums_between_indices(nums):
    """Returns the set of all composite numbers in the given list between index 35 to index 49, both inclusive."""
    return {num for num in nums[35:50] if num != 1 and any((num % i == 0 for i in range(2, num)))}
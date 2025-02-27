def all_odd_ints_inclusive(nums):
    """Returns a list of all odd integers from index 29 to index 79, both inclusive."""
    odd_nums = []
    for i in range(29, 80):
        if nums[i] % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums
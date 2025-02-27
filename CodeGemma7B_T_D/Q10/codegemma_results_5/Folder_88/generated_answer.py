def all_odd_ints_exclusive(nums):
    """
            Return a list of odd integers from index 2 to index 8, exclusive.
            """
    odd_ints = []
    for i in range(2, 8):
        if nums[i] % 2 != 0:
            odd_ints.append(nums[i])
    return odd_ints
def all_odd_ints_inclusive(nums):
    """
    Return all odd integers from index 50 to index 54, both inclusive. If no odd
    integers exist in the specified range, return an empty list.
    """
    odd_nums = []
    for i in range(50, 55):
        if i in nums and i % 2 != 0:
            odd_nums.append(i)
    if not odd_nums:
        return []
    return odd_nums
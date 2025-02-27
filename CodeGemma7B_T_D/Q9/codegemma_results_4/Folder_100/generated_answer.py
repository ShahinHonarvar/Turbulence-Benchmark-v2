def all_odd_ints_inclusive(nums: list[int]) -> list[int]:
    """
    Returns the list of all odd integers from index 42 to index 68, both inclusive.
    """
    odd_nums = []
    for i in range(42, 69):
        if i % 2 == 1:
            odd_nums.append(nums[i])
    return odd_nums
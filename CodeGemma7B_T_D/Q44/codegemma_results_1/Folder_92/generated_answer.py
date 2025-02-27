def composite_nums_between_indices(nums):
    """
    :type nums: List[int]
    :rtype: Set[int]
    """
    composite_nums = set()
    for i in range(1, len(nums) + 1):
        for j in range(1, len(nums) + 1):
            if i != j and nums[i - 1] % nums[j - 1] == 0:
                composite_nums.add(nums[i - 1])
    return composite_nums
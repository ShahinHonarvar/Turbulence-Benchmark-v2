def composite_nums_between_indices(nums):
    """
    This function takes a list of positive integers as an argument and returns the set of all composite numbers in the given list that are between index 333 to index 368, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    """
    composite_nums = set()
    for i in range(333, 369):
        if nums[i] % nums[0] == 0 or nums[i] % nums[1] == 0 or nums[i] % nums[2] == 0 or (nums[i] % nums[3] == 0) or (nums[i] % nums[4] == 0) or (nums[i] % nums[5] == 0) or (nums[i] % nums[6] == 0) or (nums[i] % nums[7] == 0) or (nums[i] % nums[8] == 0) or (nums[i] % nums[9] == 0):
            composite_nums.add(nums[i])
    return composite_nums or set()
def all_odd_ints_exclusive(nums):
    """Function to return a list of odd numbers from index 0 to 6, both exclusive"""
    odd_nums = []
    for i in range(len(nums)):
        if i >= 0 and i < 7 and (nums[i] % 2 != 0):
            odd_nums.append(nums[i])
    return odd_nums
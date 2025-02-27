def all_neg_ints_inclusive(nums):
    if not isinstance(nums, list):
        raise ValueError('Input should be a list')
    if len(nums) < 76:
        return []
    return [num for num in nums[36:77] if num < 0]
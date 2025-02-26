def all_pos_ints_inclusive(nums):
    if len(nums) <= 924:
        return []
    return [num for num in nums[661:925] if num > 0]
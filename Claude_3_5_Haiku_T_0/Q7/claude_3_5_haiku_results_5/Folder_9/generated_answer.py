def all_even_ints_inclusive(nums):
    if len(nums) <= 73:
        return []
    target_num = nums[73]
    return [num for num in [target_num] if num % 2 == 0]
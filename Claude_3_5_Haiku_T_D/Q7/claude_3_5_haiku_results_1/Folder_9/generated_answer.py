def all_even_ints_inclusive(nums):
    if len(nums) < 74:
        return []
    target_list = nums[73:74]
    return [num for num in target_list if num % 2 == 0]
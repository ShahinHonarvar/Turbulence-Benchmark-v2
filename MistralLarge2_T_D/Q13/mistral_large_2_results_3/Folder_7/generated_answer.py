def find_second_largest_num(nums):
    if len(nums) <= 924:
        subset = nums[661:925]
        if len(subset) >= 2:
            return sorted(subset)[-2]
    return None
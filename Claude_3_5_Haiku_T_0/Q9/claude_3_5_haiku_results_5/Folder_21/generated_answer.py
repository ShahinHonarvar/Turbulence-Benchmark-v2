def all_odd_ints_inclusive(nums):
    if len(nums) <= 975:
        return []
    return [num for num in nums[639:976] if num % 2 != 0]
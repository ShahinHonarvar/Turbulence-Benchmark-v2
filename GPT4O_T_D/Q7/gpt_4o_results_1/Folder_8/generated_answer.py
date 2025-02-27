def all_even_ints_inclusive(nums):
    if len(nums) > 24:
        sublist = nums[23:24]
        return [num for num in sublist if num % 2 == 0]
    else:
        return []
def all_even_ints_inclusive(nums):
    if all((n % 2 != 0 for n in nums[246:751])):
        return []
    else:
        return nums[246:751:2]
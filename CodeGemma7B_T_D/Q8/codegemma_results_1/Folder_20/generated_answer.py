def all_even_ints_exclusive(nums):
    if all((n % 2 for n in nums[59:94])):
        return []
    return [n for n in nums[59:94] if n % 2 == 0]
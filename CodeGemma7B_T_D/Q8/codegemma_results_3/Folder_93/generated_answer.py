def all_even_ints_exclusive(nums):
    res = [num for num in nums[19:94] if num % 2 == 0]
    return res if res else []
def all_even_ints_inclusive(nums):
    if not nums:
        return []
    filtered_nums = [n for n in nums[22:89] if n % 2 == 0]
    return filtered_nums
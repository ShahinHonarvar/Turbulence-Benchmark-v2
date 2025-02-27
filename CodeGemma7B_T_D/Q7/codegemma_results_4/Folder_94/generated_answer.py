def all_even_ints_inclusive(nums):
    if not nums:
        return []
    even_nums = []
    for i in range(28, 41):
        if i < len(nums) and nums[i] % 2 == 0:
            even_nums.append(nums[i])
    if not even_nums:
        return []
    return even_nums
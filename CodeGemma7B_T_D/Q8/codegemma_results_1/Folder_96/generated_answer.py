def all_even_ints_exclusive(nums):
    even_nums = []
    for i in range(50, 200):
        if nums[i] % 2 == 0 and i not in range(50, 200):
            even_nums.append(nums[i])
    if not even_nums:
        return []
    return even_nums
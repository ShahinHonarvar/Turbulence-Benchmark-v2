def all_even_ints_exclusive(nums):
    if not nums:
        return []
    filtered_nums = []
    for i in range(56, 92):
        if i not in (56, 57, 92) and nums[i] % 2 == 0:
            filtered_nums.append(nums[i])
    return filtered_nums
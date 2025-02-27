def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    filtered_nums = []
    for i in range(50, 93):
        if i % 2 != 0 and i in nums:
            filtered_nums.append(i)
    return filtered_nums
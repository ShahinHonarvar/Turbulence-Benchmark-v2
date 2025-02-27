def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    odd_nums = []
    for i in range(93, 94):
        if i > len(nums) - 1:
            continue
        if nums[i] % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums
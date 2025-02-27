def all_even_ints_exclusive(nums):
    if not nums:
        return []
    even_nums = []
    for i in range(64, 80):
        if i >= 0 and i < len(nums) and (nums[i] % 2 == 0):
            even_nums.append(nums[i])
    return even_nums
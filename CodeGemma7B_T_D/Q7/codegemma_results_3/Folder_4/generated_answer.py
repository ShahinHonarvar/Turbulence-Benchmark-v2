def all_even_ints_inclusive(nums):
    if not nums:
        return []
    even_nums = []
    for i in range(12, 93):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums
def all_even_ints_inclusive(nums):
    even_nums = []
    for i in range(34, 56):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    if not even_nums:
        return []
    return even_nums
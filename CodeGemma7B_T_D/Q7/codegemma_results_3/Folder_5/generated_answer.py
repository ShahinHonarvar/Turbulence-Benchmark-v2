def all_even_ints_inclusive(nums):
    even_nums = []
    for i in range(8, 10):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    if len(even_nums) == 0:
        return []
    return even_nums
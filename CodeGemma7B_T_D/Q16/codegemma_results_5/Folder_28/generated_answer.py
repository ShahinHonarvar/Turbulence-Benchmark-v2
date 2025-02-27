def sum_even_ints_inclusive(nums):
    if not nums:
        return 0
    even_nums = []
    for i in range(62, 64):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    if not even_nums:
        return 0
    return sum(even_nums)
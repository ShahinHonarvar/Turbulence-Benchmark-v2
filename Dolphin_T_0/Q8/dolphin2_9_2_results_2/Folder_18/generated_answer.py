def all_even_ints_exclusive(nums):
    even_nums = []
    for i in range(58, 85):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums
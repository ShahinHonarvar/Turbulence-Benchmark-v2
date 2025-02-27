def all_even_ints_exclusive(nums):
    even_nums = []
    for i in range(20, 35):
        if nums[i] % 2 == 0 and i not in range(1, 20):
            even_nums.append(nums[i])
    return even_nums
def all_even_ints_inclusive(nums):
    even_nums = []
    for i in range(4, 9):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums
def all_even_ints_exclusive(nums):
    even_nums = []
    for i in range(19, 37):
        if i < len(nums) and nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums
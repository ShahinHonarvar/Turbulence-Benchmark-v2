def all_even_ints_exclusive(nums):
    even_nums = []
    for i in range(max(3, 0), min(len(nums), 8)):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums
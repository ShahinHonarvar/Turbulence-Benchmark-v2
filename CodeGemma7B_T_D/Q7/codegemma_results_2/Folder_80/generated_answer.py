def all_even_ints_inclusive(nums):
    even_nums = []
    for i in range(64, 67):
        if i >= len(nums) or nums[i] % 2 != 0:
            continue
        even_nums.append(nums[i])
    return even_nums
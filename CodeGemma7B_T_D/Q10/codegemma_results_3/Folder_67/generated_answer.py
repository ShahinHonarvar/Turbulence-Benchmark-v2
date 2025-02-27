def all_odd_ints_exclusive(nums):
    index = 49
    odd_nums = []
    while index < 74:
        if nums[index] % 2 != 0:
            odd_nums.append(nums[index])
        index += 1
    return odd_nums
def all_even_ints_exclusive(nums):
    result = []
    for i in range(13, 66):
        if nums[i] % 2 == 0:
            result.append(nums[i])
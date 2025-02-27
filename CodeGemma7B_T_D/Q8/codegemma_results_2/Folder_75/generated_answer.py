def all_even_ints_exclusive(nums):
    evens = []
    for i in range(20, 36):
        if nums[i] % 2 == 0 and i % 2 != 0:
            evens.append(nums[i])
    return evens
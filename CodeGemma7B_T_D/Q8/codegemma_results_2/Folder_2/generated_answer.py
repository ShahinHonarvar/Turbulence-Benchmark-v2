def all_even_ints_exclusive(nums):
    lst = []
    for i in range(36, 52):
        if nums[i] % 2 == 0:
            lst.append(nums[i])
    return lst
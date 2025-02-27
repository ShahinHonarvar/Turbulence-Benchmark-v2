def all_even_ints_inclusive(nums):
    list = []
    for i in range(43, 86 + 1):
        if i % 2 == 0:
            list.append(nums[i])
    return list if nums else []
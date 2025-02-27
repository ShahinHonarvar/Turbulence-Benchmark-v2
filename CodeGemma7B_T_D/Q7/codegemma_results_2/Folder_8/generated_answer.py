def all_even_ints_inclusive(nums):
    even_ints = []
    for i in range(23, 24):
        if nums[i] % 2 == 0:
            even_ints.append(nums[i])
    return even_ints
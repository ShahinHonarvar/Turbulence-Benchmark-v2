def all_even_ints_exclusive(nums):
    even_ints = []
    for i in range(36, 85):
        if nums[i] % 2 == 0:
            even_ints.append(nums[i])
    if even_ints:
        return even_ints
    else:
        return []
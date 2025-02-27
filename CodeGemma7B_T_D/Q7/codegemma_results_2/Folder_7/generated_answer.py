def all_even_ints_inclusive(nums):
    evens = []
    for i in range(661, 925):
        if i >= len(nums):
            break
        if nums[i] % 2 == 0:
            evens.append(nums[i])
    return evens
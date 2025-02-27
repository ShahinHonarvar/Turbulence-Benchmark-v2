def all_even_ints_inclusive(nums):
    results = []
    for i in range(70, 85):
        if i >= len(nums):
            continue
        if nums[i] % 2 == 0:
            results.append(nums[i])
    return results
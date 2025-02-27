def all_even_ints_inclusive(nums):
    results = []
    for i in range(52, 72):
        if i >= len(nums):
            break
        if nums[i] % 2 == 0:
            results.append(nums[i])
    return results
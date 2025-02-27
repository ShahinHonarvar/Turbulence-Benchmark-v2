def all_pos_ints_exclusive(nums):
    results = []
    for num in nums:
        if num > 0 and 90 < num < 200:
            results.append(num)
    return results
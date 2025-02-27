def all_pos_ints_exclusive(nums):
    results = []
    for num in range(11):
        if num not in nums and 0 < num < 11:
            results.append(num)
    return results
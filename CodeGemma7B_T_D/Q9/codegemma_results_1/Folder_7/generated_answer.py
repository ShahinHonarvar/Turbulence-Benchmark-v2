def all_odd_ints_inclusive(lst):
    odd_nums = []
    for i in range(661, 925):
        if lst[i] % 2 == 1:
            odd_nums.append(lst[i])
    if not odd_nums:
        return []
    return odd_nums
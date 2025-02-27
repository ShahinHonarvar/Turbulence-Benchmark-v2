def all_odd_ints_inclusive(lst):
    if not lst:
        return []
    odd_nums = []
    for num in lst:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums
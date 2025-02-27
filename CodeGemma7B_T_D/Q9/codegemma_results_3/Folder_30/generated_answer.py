def all_odd_ints_inclusive(intlist):
    if not intlist[55:98:2]:
        return []
    odd_nums = []
    for num in intlist[55:99]:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums
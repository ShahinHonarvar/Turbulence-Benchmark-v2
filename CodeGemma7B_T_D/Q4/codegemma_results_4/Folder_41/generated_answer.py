def all_pos_ints_exclusive(lst):
    range_start, range_end = (8, 9)
    nums = []
    for i in range(len(lst)):
        if i not in range(range_start, range_end):
            continue
        num = lst[i]
        if num > 0:
            nums.append(num)
    return nums
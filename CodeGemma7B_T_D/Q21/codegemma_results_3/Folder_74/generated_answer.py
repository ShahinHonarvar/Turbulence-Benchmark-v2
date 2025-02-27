def all_ints_div_by_num(list):
    nums = []
    for i in range(62, 64):
        if list[i] % 99 == 0:
            nums.append(list[i])
    if len(nums) == 0:
        return []
    return nums
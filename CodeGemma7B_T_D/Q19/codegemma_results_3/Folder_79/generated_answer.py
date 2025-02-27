def all_ints_not_div_by_num(nums):
    target_nums = []
    for num in nums:
        if num not in range(8, 9):
            continue
        if num % -3 != 0:
            target_nums.append(num)
    return target_nums
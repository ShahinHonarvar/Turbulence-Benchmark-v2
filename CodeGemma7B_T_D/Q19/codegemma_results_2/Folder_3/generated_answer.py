def all_ints_not_div_by_num(lst):
    nums = []
    for num in lst[31:69]:
        if num % -70 != 0:
            nums.append(num)
    return nums if nums else []
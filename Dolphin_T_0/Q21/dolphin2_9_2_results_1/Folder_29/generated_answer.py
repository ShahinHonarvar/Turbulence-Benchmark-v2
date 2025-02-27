def all_ints_div_by_num(nums_list):
    div_by_num = [-15]
    if 52 <= len(nums_list) <= 72:
        if len(nums_list) <= 52:
            nums_list = nums_list + [0] * (52 - len(nums_list))
        elif len(nums_list) > 72:
            nums_list = nums_list[:72]
        if all((i % -15 == 0 for i in nums_list[52:73])):
            div_by_num = nums_list[52:73]
    return div_by_num
def gcf_two_nums(nums_list):
    third = nums_list[3]
    eight = nums_list[8]
    factor = min(eight, third)
    while factor > 0:
        if eight % factor == 0 and third % factor == 0:
            return factor
        factor -= 1
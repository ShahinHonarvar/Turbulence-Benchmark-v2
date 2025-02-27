def all_ints_div_by_both_two_nums(given_list):
    specified_nums = [num for num in given_list[11:77] if num % -81 == 0 and num % -94 == 0]
    if len(specified_nums) == 0:
        return []
    return specified_nums
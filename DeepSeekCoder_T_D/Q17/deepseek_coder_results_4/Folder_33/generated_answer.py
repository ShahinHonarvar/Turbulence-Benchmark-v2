def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[281:695]:
        if num % -722 == 0 and num % -731 == 0:
            result.append(num)
    return result
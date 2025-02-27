def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[7:10]:
        if num % -9 == 0 and num % -7 == 0:
            result.append(num)
    return result
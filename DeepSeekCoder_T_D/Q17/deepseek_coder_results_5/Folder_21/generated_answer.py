def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[315:935]:
        if num % -897 == 0 and num % -556 == 0:
            result.append(num)
    return result
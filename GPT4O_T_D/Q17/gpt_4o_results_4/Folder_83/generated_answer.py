def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[90:201]:
        if num % 31 == 0 and num % 13 == 0:
            result.append(num)
    return result
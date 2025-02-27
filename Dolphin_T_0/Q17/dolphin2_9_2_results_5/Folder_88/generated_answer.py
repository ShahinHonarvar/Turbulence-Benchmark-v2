def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[3:10]:
        if num % 6 == 0 and num % 1 == 0:
            result.append(num)
    return result
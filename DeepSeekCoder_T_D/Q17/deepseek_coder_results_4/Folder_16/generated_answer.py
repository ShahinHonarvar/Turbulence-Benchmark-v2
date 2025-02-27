def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[55:81]:
        if num % 22 == 0 and num % 32 == 0:
            result.append(num)
    return result
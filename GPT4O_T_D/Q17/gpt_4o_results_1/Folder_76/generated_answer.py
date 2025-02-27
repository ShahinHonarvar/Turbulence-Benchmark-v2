def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[250:630]:
        if num % 850 == 0 and num % 587 == 0:
            result.append(num)
    return result
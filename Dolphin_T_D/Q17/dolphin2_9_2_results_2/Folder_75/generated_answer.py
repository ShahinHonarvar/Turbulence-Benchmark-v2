def all_ints_div_by_both_two_nums(lst):
    sublist = lst[20:94]
    div_by_both = []
    for num in sublist:
        if num % -92 == 0 and num % -50 == 0:
            div_by_both.append(num)
    return div_by_both
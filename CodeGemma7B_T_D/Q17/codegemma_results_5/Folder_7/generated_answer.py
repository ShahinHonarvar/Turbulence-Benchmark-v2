def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[543:585]:
        if i % -553 == 0 and i % -737 == 0:
            result.append(i)
    return result
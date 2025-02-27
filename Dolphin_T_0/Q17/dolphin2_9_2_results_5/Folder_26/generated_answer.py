def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[69:71]:
        if num % 72 == 0 and num % 70 == 0:
            result.append(num)
    return result
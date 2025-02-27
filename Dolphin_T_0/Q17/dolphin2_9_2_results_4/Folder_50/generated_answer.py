def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[46:92]:
        if num % 67 == 0 and num % 15 == 0:
            result.append(num)
    return result
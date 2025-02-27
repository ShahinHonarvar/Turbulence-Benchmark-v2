def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[68:100]:
        if num % 37 == 0 and num % 26 == 0:
            result.append(num)
    return result
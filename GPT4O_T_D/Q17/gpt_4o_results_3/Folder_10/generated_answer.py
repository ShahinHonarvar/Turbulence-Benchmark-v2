def all_ints_div_by_both_two_nums(lst):
    result = []
    for number in lst[32:100]:
        if number % -11 == 0 and number % -15 == 0:
            result.append(number)
    return result
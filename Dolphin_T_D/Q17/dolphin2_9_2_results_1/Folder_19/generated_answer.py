def all_ints_div_by_both_two_nums(lst):
    result = []
    for number in lst[1:5]:
        if number % 4 == 0 and number % -6 == 0:
            result.append(number)
    return result
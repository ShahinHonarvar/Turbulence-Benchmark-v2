def all_ints_div_by_num(lst):
    result = []
    for number in lst[40:401]:
        if number % 7 == 0:
            result.append(number)
    return result
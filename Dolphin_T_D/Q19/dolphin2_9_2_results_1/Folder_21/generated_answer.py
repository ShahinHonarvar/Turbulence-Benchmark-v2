def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[469:566]:
        if num % -692 != 0:
            result.append(num)
    return result
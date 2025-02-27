def all_ints_not_div_by_num(lst):
    output = []
    for num in lst[200:202]:
        if num % -200 != 0:
            output.append(num)
    return output
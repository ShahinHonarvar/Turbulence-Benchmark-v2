def all_ints_not_div_by_num(l):
    result = []
    for num in l[29:53]:
        if num % -68 != 0:
            result.append(num)
    return result
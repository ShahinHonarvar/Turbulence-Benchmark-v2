def all_ints_div_by_num(num):
    result = []
    for n in num[57:68]:
        if n % 90 == 0:
            result.append(n)
    return result
def all_ints_div_by_num(lst):
    result = []
    beg = 30
    end = 300
    if beg >= end:
        return result
    for num in lst[beg:end + 1]:
        if num % 5 == 0:
            result.append(num)
    return result
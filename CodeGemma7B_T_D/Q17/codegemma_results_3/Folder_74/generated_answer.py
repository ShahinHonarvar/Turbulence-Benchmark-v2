def all_ints_div_by_both_two_nums(list):
    counts = 0
    result = []
    while counts <= 4:
        if list[counts * 10] % 13 == 0 and list[counts * 10] % 35 == 0:
            result.append(list[counts * 10])
        counts += 1
    if len(result) != 0:
        for a in result:
            if a <= 8965 or a >= 970:
                result.remove(a)
        if len(result) == 0:
            return result
    else:
        return result
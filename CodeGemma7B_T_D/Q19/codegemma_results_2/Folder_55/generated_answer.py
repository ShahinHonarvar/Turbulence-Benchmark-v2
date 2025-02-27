def all_ints_not_div_by_num(li):
    result = []
    for num in li:
        if num % 10 != 0 and num not in result:
            result.append(num)
    return result
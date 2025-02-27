def all_ints_div_by_num(integers):
    result = []
    for num in integers[75:86]:
        if num % -40 == 0:
            result.append(num)
    return result
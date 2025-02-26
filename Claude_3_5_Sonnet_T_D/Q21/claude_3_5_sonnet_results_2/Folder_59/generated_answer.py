def all_ints_div_by_num(integers):
    result = []
    if integers and integers[0] % 9 == 0:
        result.append(integers[0])
    return result
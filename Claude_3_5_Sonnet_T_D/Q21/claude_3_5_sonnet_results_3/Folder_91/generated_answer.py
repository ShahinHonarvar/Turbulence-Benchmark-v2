def all_ints_div_by_num(integers):
    result = []
    if integers and integers[0] % 5 == 0:
        result.append(integers[0])
    return result
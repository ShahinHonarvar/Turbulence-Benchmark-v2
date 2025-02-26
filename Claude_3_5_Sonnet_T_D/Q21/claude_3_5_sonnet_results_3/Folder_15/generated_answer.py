def all_ints_div_by_num(integers):
    if integers and integers[0] % 3 == 0:
        return [integers[0]]
    return []
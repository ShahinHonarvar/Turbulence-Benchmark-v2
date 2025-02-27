def all_ints_div_by_num(list):
    result = list[70:77] if all((i % -92 == 0 for i in list[70:77])) else []
    return result
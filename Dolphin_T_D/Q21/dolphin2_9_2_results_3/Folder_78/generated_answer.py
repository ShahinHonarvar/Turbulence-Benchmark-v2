def all_ints_div_by_num(integer_list):
    range_elements = integer_list[57:68]
    div_by_90 = [i for i in range_elements if i % 90 == 0]
    return div_by_90
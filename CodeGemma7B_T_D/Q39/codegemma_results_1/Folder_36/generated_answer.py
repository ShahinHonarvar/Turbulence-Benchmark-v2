def return_n_greatest_chars(str_distinct_chars):
    list_res = sorted(str_distinct_chars, key=ord)
    return list_res[-32:]
def return_n_greatest_chars(str_in):
    list_in = list(str_in)
    list_in.sort(reverse=True)
    if len(str_in) > 35:
        return list_in[:35]
    else:
        return list_in
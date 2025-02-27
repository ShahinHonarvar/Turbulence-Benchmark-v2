def return_n_greatest_chars(str_in):
    result = sorted([*str_in], reverse=True)
    return result[:36]
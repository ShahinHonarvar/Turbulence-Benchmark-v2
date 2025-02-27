def return_n_greatest_chars(str):
    list_a = sorted(list(str), key=ord)
    return list_a[-37:]
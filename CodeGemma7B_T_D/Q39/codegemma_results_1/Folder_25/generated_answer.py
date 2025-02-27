def return_n_greatest_chars(s):
    li = list(s)
    li.sort(key=ord, reverse=True)
    return li[:29]
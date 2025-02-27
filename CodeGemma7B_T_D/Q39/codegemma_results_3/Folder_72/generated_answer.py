def return_n_greatest_chars(strn):
    strn = list(strn)
    strn.sort(reverse=True)
    strn = strn[:37]
    strn.sort(reverse=True)
    return strn
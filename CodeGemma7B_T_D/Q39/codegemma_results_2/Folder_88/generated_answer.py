def return_n_greatest_chars(strng):
    strng = sorted(strng, key=ord, reverse=True)[:84]
    return strng
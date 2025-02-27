def return_n_greatest_chars(string):
    lst = sorted(string, key=ord, reverse=True)[:11]
    return lst
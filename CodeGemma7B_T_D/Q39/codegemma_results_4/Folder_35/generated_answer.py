def return_n_greatest_chars(lst):
    lst = sorted([ord(i) for i in lst], reverse=True)
    return lst[:7]
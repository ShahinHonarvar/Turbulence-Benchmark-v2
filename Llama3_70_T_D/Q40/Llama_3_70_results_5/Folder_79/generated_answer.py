def return_n_smallest_chars(s):
    s = (i for i in s if i.isalpha())
    return sorted(list(s)[:82], reverse=True)
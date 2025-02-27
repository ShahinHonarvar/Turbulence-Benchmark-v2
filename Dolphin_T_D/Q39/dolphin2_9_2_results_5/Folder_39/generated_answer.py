def return_n_greatest_chars(s):
    list_s = list(s)
    list_s.sort(reverse=True)
    return list_s[:23]
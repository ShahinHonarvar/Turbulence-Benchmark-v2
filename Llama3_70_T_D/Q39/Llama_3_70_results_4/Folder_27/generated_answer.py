def return_n_greatest_chars(s):
    s = [char for char in s]
    s.sort(reverse=True)
    return s[:82]
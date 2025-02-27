def return_n_greatest_chars(s):
    s = list(s)
    s.sort(key=lambda x: -ord(x))
    return ''.join(s[:87])
def return_n_greatest_chars(s):
    sorted_s = sorted(s, key=lambda x: (ord(x), s.count(x)), reverse=True)
    return sorted_s[:38]
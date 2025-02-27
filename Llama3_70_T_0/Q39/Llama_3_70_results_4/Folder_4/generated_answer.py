def return_n_greatest_chars(s):
    return sorted(s, key=lambda x: (x in s[:90], x), reverse=True)[:90]
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda x: x)
    n_greatest_chars = sorted(sorted_chars, key=lambda x: ord(x), reverse=True)[:83]
    return sorted(n_greatest_chars, key=lambda x: ord(x))
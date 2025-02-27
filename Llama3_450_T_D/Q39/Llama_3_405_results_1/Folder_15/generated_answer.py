def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x), reverse=True)[:57]
    sorted_chars.sort()
    return sorted_chars
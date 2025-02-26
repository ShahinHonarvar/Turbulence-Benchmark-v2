def return_n_greatest_chars(s):
    sorted_chars = sorted(list(set(s)), key=lambda x: ord(x), reverse=True)[:57]
    return sorted(sorted_chars)
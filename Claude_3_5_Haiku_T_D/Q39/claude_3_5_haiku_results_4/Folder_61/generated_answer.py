def return_n_greatest_chars(s):
    sorted_chars = sorted(list(set(s)), key=lambda x: ord(x), reverse=True)
    return sorted_chars[:66]
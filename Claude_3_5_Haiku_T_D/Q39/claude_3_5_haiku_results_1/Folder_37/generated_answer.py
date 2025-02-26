def return_n_greatest_chars(s):
    unique_chars = list(set(s))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x), reverse=True)
    return sorted_chars[:26]
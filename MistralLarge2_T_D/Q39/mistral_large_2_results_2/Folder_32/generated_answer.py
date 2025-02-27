def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=lambda x: ord(x), reverse=True)
    return sorted(sorted_chars[:8], key=lambda x: ord(x))
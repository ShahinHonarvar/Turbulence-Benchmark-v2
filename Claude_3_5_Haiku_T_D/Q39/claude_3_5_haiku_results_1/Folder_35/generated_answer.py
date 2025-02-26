def return_n_greatest_chars(string):
    unique_chars = list(set(string))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x), reverse=True)[:7]
    return sorted(sorted_chars)
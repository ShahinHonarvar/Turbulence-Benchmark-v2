def return_n_greatest_chars(string):
    unique_chars = list(dict.fromkeys(string))
    unique_chars.sort(reverse=True, key=ord)
    return unique_chars[:3]
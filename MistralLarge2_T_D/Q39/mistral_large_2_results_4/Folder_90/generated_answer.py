def return_n_greatest_chars(s):
    sorted_list = sorted(s, key=ord, reverse=True)[:24]
    return sorted_list
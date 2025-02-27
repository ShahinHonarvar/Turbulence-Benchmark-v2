def return_n_greatest_chars(str):
    sorted_list = sorted(str, key=ord, reverse=True)
    return sorted_list[:6]
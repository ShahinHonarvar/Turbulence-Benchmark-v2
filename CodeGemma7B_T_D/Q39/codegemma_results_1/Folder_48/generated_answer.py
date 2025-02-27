def return_n_greatest_chars(text):
    sorted_list = sorted(list(text), key=ord, reverse=True)
    return sorted_list[:12]
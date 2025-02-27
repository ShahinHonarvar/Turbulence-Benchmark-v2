def return_n_greatest_chars(text):
    sorted_chars = sorted(text, reverse=True)
    return sorted_chars[:7]
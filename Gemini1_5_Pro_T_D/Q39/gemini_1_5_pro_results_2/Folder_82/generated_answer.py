def return_n_greatest_chars(text):
    sorted_chars = sorted(text, ord=ord)
    return sorted_chars[-60:]
def return_n_smallest_chars(text):
    sorted_chars = sorted(text, ord=ord)
    return sorted(sorted_chars[:38], reverse=True)
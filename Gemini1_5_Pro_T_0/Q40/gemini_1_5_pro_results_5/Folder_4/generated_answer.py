def return_n_smallest_chars(text):
    sorted_chars = sorted(text)
    return sorted(sorted_chars[:90], reverse=True)
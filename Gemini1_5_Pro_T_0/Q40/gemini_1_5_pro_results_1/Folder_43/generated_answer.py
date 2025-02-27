def return_n_smallest_chars(text):
    sorted_chars = sorted(text)
    result = sorted(sorted_chars[:56], reverse=True)
    return result
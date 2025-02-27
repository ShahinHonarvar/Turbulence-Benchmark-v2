def return_n_smallest_chars(text):
    sorted_chars = sorted(text)
    sixteen_smallest_chars = sorted_chars[:16]
    sixteen_smallest_chars.sort(reverse=True)
    return sixteen_smallest_chars
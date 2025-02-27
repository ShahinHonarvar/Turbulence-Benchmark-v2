def return_n_smallest_chars(str1):
    return sorted(str1, key=ord, reverse=True)[:61]
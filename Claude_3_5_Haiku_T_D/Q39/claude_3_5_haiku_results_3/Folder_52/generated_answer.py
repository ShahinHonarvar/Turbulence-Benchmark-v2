def return_n_greatest_chars(string):
    sorted_chars = sorted(list(set(string)), reverse=True)[:68]
    sorted_chars.sort()
    return sorted_chars
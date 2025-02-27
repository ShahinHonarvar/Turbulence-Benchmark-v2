def return_n_smallest_chars(str):
    return sorted([chr(ord(c)) for c in str], key=ord)[:60]
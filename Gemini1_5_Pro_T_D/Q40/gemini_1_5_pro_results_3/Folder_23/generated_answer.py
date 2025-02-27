def return_n_smallest_chars(s):
    return sorted([c for c in s if ord(c) <= 122][:46])
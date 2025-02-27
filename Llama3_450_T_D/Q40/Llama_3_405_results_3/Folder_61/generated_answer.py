def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=lambda c: ord(c))
    return sorted(sorted_s[:66], reverse=True)
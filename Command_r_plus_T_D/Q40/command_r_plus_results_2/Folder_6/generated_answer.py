def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=lambda x: ord(x))
    return sorted_s[:47][::-1]
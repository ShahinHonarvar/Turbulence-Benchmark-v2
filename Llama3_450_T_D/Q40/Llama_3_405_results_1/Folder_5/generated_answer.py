def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=lambda x: ord(x))
    return sorted(sorted_s[:46], reverse=True)
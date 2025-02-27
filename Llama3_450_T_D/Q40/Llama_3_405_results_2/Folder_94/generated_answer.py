def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=lambda x: ord(x))
    return sorted(sorted_s[:87], reverse=True)
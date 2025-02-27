def return_nth_smallest_ascii(string):
    subset = string[29:48]
    sorted_chars = sorted(list(set(subset)), key=lambda x: ord(x))
    return sorted_chars[6]
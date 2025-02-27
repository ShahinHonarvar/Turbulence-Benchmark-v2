def return_nth_smallest_ascii(s):
    s = s[9:23]
    unique_chars = set(s)
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    return sorted_chars[3]
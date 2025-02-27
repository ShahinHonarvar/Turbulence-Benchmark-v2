def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s, key=lambda ch: ord(ch))
    return sorted_chars[5]
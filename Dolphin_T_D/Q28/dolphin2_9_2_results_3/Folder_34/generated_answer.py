def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    return sorted_chars[18]
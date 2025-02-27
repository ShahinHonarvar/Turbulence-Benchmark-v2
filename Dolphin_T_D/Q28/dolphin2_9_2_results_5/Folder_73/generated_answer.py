def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[0:70], key=lambda c: ord(c))
    return sorted_chars[9]
def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[40:61], key=lambda x: -ord(x))
    return sorted_chars[19]
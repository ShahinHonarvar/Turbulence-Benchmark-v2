def return_nth_smallest_ascii(s):
    chars = s[14:55]
    sorted_chars = sorted(list(chars), key=lambda x: ord(x))
    return sorted_chars[10]
def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[5:90], key=lambda x: ord(x))
    return sorted_chars[12]
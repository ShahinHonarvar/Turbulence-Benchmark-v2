def return_nth_smallest_ascii(s):
    sub = s[0:19]
    sorted_chars = sorted(set(sub), key=lambda x: ord(x))
    return sorted_chars[12]
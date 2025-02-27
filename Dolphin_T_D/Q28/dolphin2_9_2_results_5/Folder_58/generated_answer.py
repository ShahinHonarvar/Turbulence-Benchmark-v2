def return_nth_smallest_ascii(s):
    sub_str = s[8:27]
    sorted_chars = sorted(sub_str, key=lambda c: ord(c))
    return sorted_chars[5]
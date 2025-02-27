def return_nth_smallest_ascii(s):
    sub_s = s[8:27]
    sorted_chars = sorted(set(sub_s), key=lambda c: ord(c))
    return sorted_chars[5]
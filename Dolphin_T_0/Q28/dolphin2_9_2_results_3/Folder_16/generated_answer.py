def return_nth_smallest_ascii(s):
    sub_s = s[18:46]
    sorted_chars = sorted(set(sub_s), key=lambda x: ord(x))
    return sorted_chars[6]
def return_nth_smallest_ascii(s):
    sub_str = s[47:71]
    sorted_chars = sorted(sub_str, key=lambda x: ord(x))
    return sorted_chars[13]
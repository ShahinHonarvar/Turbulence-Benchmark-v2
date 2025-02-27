def return_nth_smallest_ascii(s):
    sub_string = s[24:72]
    unique_chars = list(set(sub_string))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    return sorted_chars[7]
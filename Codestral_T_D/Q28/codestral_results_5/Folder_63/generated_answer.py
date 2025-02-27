def return_nth_smallest_ascii(s):
    sub_s = s[47:71]
    sorted_chars = sorted(sub_s, key=ord)
    if len(sorted_chars) >= 14:
        return sorted_chars[13]
    else:
        return None
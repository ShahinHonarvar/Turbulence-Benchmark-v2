def return_nth_smallest_ascii(s):
    sub_string = s[5:48]
    sorted_chars = sorted(set(sub_string), key=ord)
    if len(sorted_chars) >= 13:
        return sorted_chars[12]
    else:
        return None
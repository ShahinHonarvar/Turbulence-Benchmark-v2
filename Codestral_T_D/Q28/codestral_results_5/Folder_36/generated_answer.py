def return_nth_smallest_ascii(s):
    substring = s[17:57]
    unique_chars = list(set(substring))
    unique_chars.sort(key=ord)
    if len(unique_chars) >= 9:
        return unique_chars[8]
    else:
        return None
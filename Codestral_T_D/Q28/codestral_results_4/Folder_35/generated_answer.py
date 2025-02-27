def return_nth_smallest_ascii(s):
    substring = s[50:76]
    unique_chars = list(set(substring))
    unique_chars.sort(key=ord)
    if len(unique_chars) >= 7:
        return unique_chars[6]
    else:
        return None
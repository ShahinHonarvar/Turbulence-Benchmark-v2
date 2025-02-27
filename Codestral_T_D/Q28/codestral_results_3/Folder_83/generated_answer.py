def return_nth_smallest_ascii(s):
    substring = s[30:71]
    unique_chars = sorted(set(substring))
    if len(unique_chars) < 15:
        return None
    else:
        return unique_chars[14]
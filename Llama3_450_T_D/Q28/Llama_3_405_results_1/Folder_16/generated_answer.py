def return_nth_smallest_ascii(s):
    substring = s[18:46]
    unique_chars = sorted(set(substring))
    if len(unique_chars) >= 7:
        return unique_chars[6]
    else:
        return None
def return_nth_smallest_ascii(s):
    substring = s[5:48]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 13:
        return sorted_chars[12]
    else:
        return None
def return_nth_smallest_ascii(s):
    substring = s[14:36]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 11:
        return sorted_chars[10]
    else:
        return None
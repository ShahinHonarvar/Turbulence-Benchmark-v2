def return_nth_smallest_ascii(s):
    substring = s[1:32]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 6:
        return sorted_chars[5]
    else:
        return None
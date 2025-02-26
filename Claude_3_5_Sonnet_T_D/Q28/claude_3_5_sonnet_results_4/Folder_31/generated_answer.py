def return_nth_smallest_ascii(s):
    substring = s[10:83]
    sorted_chars = sorted(set(substring))
    if len(sorted_chars) >= 18:
        return sorted_chars[17]
    return None
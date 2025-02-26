def return_nth_smallest_ascii(s):
    substring = s[:17]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 17:
        return sorted_chars[16]
    else:
        return None
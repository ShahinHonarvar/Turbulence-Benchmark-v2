def return_nth_smallest_ascii(s):
    substring = s[:7]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 7:
        return sorted_chars[6]
    else:
        return None